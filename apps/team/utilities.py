from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#


def send_invitation(to_emails, code, team):
    from_email = settings.DEFAULT_EMAIL_FROM
    acceptation_url = settings.ACCEPTATION_URL
    api_key = settings.EMAIL_HOST_PASSWORD

    subject = 'Invitation to Minutos'
    text_content = 'Invitation to Minutos. Your code is: %s' % code
    html_content = render_to_string(
        'team/email_invitation.html', {'code': code, 'team': team, 'acceptation_url': acceptation_url})
    message = Mail(
        from_email,
        to_emails,
        subject,
        text_content,
        html_content
    )

    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e)


def send_invitation_accepted(team, invitation):
    api_key = settings.EMAIL_HOST_PASSWORD
    from_email = settings.DEFAULT_EMAIL_FROM
    subject = 'Invitation accepted'
    text_content = 'Your invitation was accepted'
    to_emails = team.created_by.email
    html_content = render_to_string(
        'team/email_accepted_invitation.html', {'team': team, 'invitation': invitation})
    message = Mail(
        from_email,
        [to_emails],
        subject,
        text_content,
        html_content
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e)

    # msg = EmailMultiAlternatives(subject, text_content, from_email, [
    #                              team.created_by.email])
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()
