def test_case():
    yield """
Bad email address on order ack # 602278
Sent: Tue, 31 Mar 2015 12:20:41 -0600
From: user@example.com
To: user@example.com
Subject: Fwd: Bad email on order ack # 602278
Body: Description##Bad email address on order ack # 602278##
Service##ERP##
CI##APP_PAM_PRMS##
Staff##Name Surname##
Impact##Low##
Urgency##Low##

It was just the letter S as the email address.
Notified Name Surname.

This has been completed

---------- Forwarded message ----------
From: Name Surname <user@example.com>
Date: Tue, Mar 31, 2015 at 12:19 PM
Subject: Bad email on order ack # 602278
To: Name Surname <user@example.com>


Hi Name Surname,
...
Please try again.

Thanks,

Name Surname
www.petzl.com • www.petzldealer.com
"""
    

    yield """
Sent: Tue, 1 Jul 2014 16:32:41 +0200
From:user@example.com
To: user@example.com
Subject: Re: Service Request #00292653 has been created
Body: Hello,

Je n'ai pas de nouvelles de ce ticket, et ça commence à urger.
Vous pouvez me tenir au courant ?

J'ai essayé d'ajouter une note sur la requête dans Take IT easy, mais ma
note n'a pas été enregistrée (le bouton "add" vide le champ, mais n'ajoute
pas la note)
[image: Inline images 1]

--
Name Surname
Chef de projet web
www.petzl.com • www.petzldealer.com


On 17 June 2014 11:22, example Take IT Easy <user@example.com> wrote:

>  Hello,
>
> Service Request #00292653 has been created and assigned to the Service
...
> Thank you,
>
> Service Desk Team
>
"""

    yield """
Cognos Migration Incomplete
Sent: Wed, 15 Apr 2015 11:12:51 -0600
From: user@petzl.com
To: user@petzl.com
Subject: Cognos Migration Incomplete
Body: Hello,

For C8 under domain PetzlAM and PetzlFR the migration looks incomplete ,
not all of my reports are under Accounting.  Under domain PetzlAM (Old) my
reports are there.
Is this what you would expect or should I be seeing under PetzlFR all of my
reports at this time?
'
Thanks,

*Name Surname*
Senior Financial Accountant
*Organization Name*
tel 123.456.7890
toll free 123.456.7890 x1234
fax 123.456.7890
user@example.com
www.petzldealer.com
"""
