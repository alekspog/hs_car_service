from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from collections import deque

change_oil_queue = deque()
inflate_tires_queue = deque()
diagnostics_queue = deque()
ticket = 0
next_ticket = 0


class MenuView(View):
    links = [
        {
            'url': '/get_ticket/change_oil',
            'title': 'Change oil'
        },
        {
            'url': '/get_ticket/inflate_tires',
            'title': 'Inflate tires'
        },
        {
            'url': '/get_ticket/diagnostic',
            'title': 'Diagnostic'
        }
    ]
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html', context={'links': self.links})


class ChangeOilView(View):
    def get(self, request, *args, **kwargs):
        global ticket
        ticket = ticket + 1
        time = len(change_oil_queue) * 2
        change_oil_queue.append(ticket)
        return render(request, 'get_ticket.html', context={'number': ticket, 'time': time})


class InflateTiresView(View):
    def get(self, request, *args, **kwargs):
        global ticket
        ticket = ticket + 1
        time = len(change_oil_queue) * 2 + len(inflate_tires_queue) * 5
        inflate_tires_queue.append(ticket)
        return render(request, 'get_ticket.html', context={'number': ticket, 'time': time})


class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        global ticket
        ticket = ticket + 1
        time = len(change_oil_queue) * 2 + len(inflate_tires_queue) * 5 + len(diagnostics_queue) * 30
        diagnostics_queue.append(ticket)
        return render(request, 'get_ticket.html', context={'number': ticket, 'time': time})


class NextView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'next.html', context={
            'ticket_number': next_ticket
        })


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'processing.html',
                      context={
                        'oil_queue': len(change_oil_queue),
                        'tires_queue': len(inflate_tires_queue),
                        'diagnostic_queue': len(diagnostics_queue)
                      })

    def post(self, request, *args, **kwargs):
        global next_ticket
        if len(change_oil_queue) > 0:
            next_ticket = change_oil_queue[0]
            change_oil_queue.popleft()
        elif len(inflate_tires_queue) > 0:
            next_ticket = inflate_tires_queue[0]
            inflate_tires_queue.popleft()
        elif len(diagnostics_queue) > 0:
            next_ticket = diagnostics_queue[0]
            diagnostics_queue.popleft()
        else:
            next_ticket = 0

        return redirect('/next')


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Welcome to the Hypercar Service!")
