from django.shortcuts import render, redirect
from django.http import HttpRequest
import json
from .forms import Add_New, Edit_Article
from datetime import datetime
from blog import utils

def homePage(request):
    with open("details.json", "r") as json_file:
        try:
            details = json.load(json_file)
        except json.JSONDecodeError as e:
            details = []
    return render(request, "home.html", {"details_val": details})


def articlePage(request, id):
    with open("details.json", "r") as json_file:
        try:
            details = json.load(json_file)
        except json.JSONDecodeError as e:
            details = []
    for i in details:
        if i["SrNo"] == id:
            article = i
            break
    return render(request, "article.html", {"article": article})


@utils.basic_auth
def adminPage(request):
    with open("details.json", "r") as json_file:
        try:
            details = json.load(json_file)
        except json.JSONDecodeError as e:
            details = []
        values = []
        for i in details:
            if i["Created_by"] == request.get_user_name:
                values.append(i)
        return render(request, "admin_page.html", {"detail_val": values})


@utils.basic_auth
def editPage(request, id):
    with open("details.json", "r+") as json_file:
        try:
            details = json.load(json_file)
        except json.JSONDecodeError as e:
            details = []

        if request.method == "POST":
            edit_form = Edit_Article(request.POST)
            # print("Inside Method")
            # print("Errorrs ::::::::::",edit_form.errors)
            # print("Form ::::::::", edit_form.data)
            if edit_form.is_valid():
                print("Inside Valid")
                title = edit_form.cleaned_data['title']
                content = edit_form.cleaned_data['content']
                print("Content::::::::::", content)
                for i in details:
                    if i["SrNo"] == id:
                        i['Heading'] = title
                        i["Content"] = content
                        break
                json_file.seek(0)
                json.dump(details, json_file)
                json_file.truncate()
            return redirect("/")
        edit_form = Edit_Article()
        for i in details:
            if i["SrNo"] == id:
                edit_form.custom(obj=i)
                date = i["Date"]
        return render(request, "edit.html", {"edit_article": edit_form, "id": id, "date": date})


@utils.basic_auth
def newPage(request):
    with open("details.json", "r+") as json_file:
        try:
            details = json.load(json_file)
        except json.JSONDecodeError as e:
            details = []
        if len(details) == 0:
            last_sr = 1
        else:
            last_sr = details[-1]["SrNo"]
        new_form = Add_New()
        formatted = datetime.now().strftime("%B %d, %Y")

        if request.method == "POST":
            new_form = Add_New(request.POST)
            if new_form.is_valid():
                title = new_form.cleaned_data['title']
                content = new_form.cleaned_data['content']
                details.append({"SrNo": last_sr + 1, "Heading": title,
                                "Date": formatted, "Content": content, "Created_by": request.get_user_name})
                json_file.seek(0)
                json.dump(details, json_file, indent=3)
                json_file.truncate()
                return redirect('/admin_page')
        return render(request, "new.html", {"new_form": new_form, "formatted": formatted})


@utils.basic_auth
def deletePage(request, id):
    with open("details.json", "r+") as json_file:
        try:
            details = json.load(json_file)
        except json.JSONDecodeError as e:
            details = []
        for i in details:
            if i["SrNo"] == id:
                details.remove(i)
                break
        json_file.seek(0)
        json.dump(details, json_file)
        json_file.truncate()
        return redirect('/admin_page')
