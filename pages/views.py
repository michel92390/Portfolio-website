# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from skills.models import Skill
from about.models import About
from stats.models import Stat
from projects.models import Project

# Create your views here.
def index(request):
    skills = Skill.objects.all()
    abouts = About.objects.all()
    stats = Stat.objects.all()
    projects = Project.objects.all()
    context = {
        'skills': skills,
        'abouts': abouts,
        'stats': stats,
        'projects': projects
    }

    return render(request, 'pages/index.html', context)
