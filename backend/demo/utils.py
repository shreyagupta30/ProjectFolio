from django.shortcuts import render
import os
import requests
import json
from .models import Project, MLHMember, Commit
from django.http import JsonResponse
from django.http import HttpResponse

# gets access token from environment variables
api_key = os.environ.get('MLHTOKEN')


def github_api(url):
    """Call github API v3 with a get request"""
    api_key = os.environ.get('MLHTOKEN')
    print(api_key)
    return requests.get(url,
                        headers={'Content-Type': 'application/json',
                                 'Authorization': 'token {}'.format(api_key)})


def get_user_from_github(request):
    """gets a list of all the users"""
    url = "https://api.github.com/orgs/mlh-fellowship/members"
    all_users = []
    for i in range(1, 13):
        each_url = url + '?page=' + str(i)
        result = github_api(each_url)
        print(result)
        for user in result.json():
            all_users.append(user['login'])
            member = MLHMember.objects.create(
                name=user['login'],
                avatar_url=user['avatar_url'],
                member_url=user['html_url'],
            )
            member.save()

    return HttpResponse('')


def get_list_of_all_forks():
    """gets the list of all the forked repos"""
    url = "https://api.github.com/orgs/mlh-fellowship/repos?type=forks"
    all_repos = []
    for i in range(1, 6):
        each_url = url + '&page=' + str(i)
        result = github_api(each_url)
        for repo in result.json():
            all_repos.append(repo['name'])
    return all_repos


def number_of_forks():
    """Number of Forks"""
    return len(get_list_of_all_forks())


def total_member_countries():
    """Numebr of Countries Fellows have part from"""

    url = "https://api.github.com/orgs/mlh-fellowship/members"
    all_users_countries = []
    for i in range(1, 13):
        each_url = url + '?page=' + str(i)
        result = github_api(each_url)
        print(result)
        for user in result.json():
            user_url = user['url']
            user_details = github_api(user_url)
            print(user_details)
            all_users_countries.append(user_details.json()['location'])
            print(user_details.json()['location'])

    return set(all_users_countries)


def get_all_forks(request):
    """gets the list of all the forked repos"""
    url = "https://api.github.com/orgs/mlh-fellowship/repos?type=forks"
    all_repos = []
    for i in range(1, 6):
        each_url = url + '&page=' + str(i)
        result = github_api(each_url)
        for repo in result.json():
            each_repo = []
            each_repo.append(repo['name'])
            each_repo.append(repo['description'])

            parent = github_api(repo['url'])
            parent = parent.json()

            avatar = parent['parent']['owner']['avatar_url']
            commits_url = parent['source']['commits_url']
            each_repo.append(avatar)

            each_repo.append(repo['html_url'])

            project = Project.objects.create(name=each_repo[0],
                                             description=each_repo[1],
                                             avatar_url=each_repo[2],
                                             project_url=each_repo[3],
                                             commits_url=commits_url)
            project.save()
            print(each_repo)

            all_repos.append(each_repo)

    json_object = json.dumps(all_repos, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    return HttpResponse('')


def map_commits_with_member(all_members, response, project_name):

    for r in response.json():
        try:
            if r['author']['login'] in all_members:

                commit = Commit.objects.create(
                    author=r['author']['login'],
                    project=project_name,
                    description=r['commit']['message'],
                    commit_url=r['html_url'],
                )
                commit.save()
        except:
            pass
    return


def get_commits(request):
    members = MLHMember.objects.all()
    all_members = []
    for member in members:
        all_members.append(member.name)

    projects = Project.objects.all()
    for project in projects:
        project_name = project.name
        commit_url = project.commits_url
        url = commit_url[:len(commit_url) - 6] + "?since=2020-06-01T00:00:00Z"
        print(url)

        response = github_api(url)
        map_commits_with_member(all_members, response, project_name)
        while response.links.get('next'):
            response = github_api(response.links['next']['url'])
            print(response)
            map_commits_with_member(all_members, response, project_name)

    return HttpResponse(all_members)
