def test_case():
    yield """
Bad email address on order ack # 602278
Sent: Tue, 31 Mar 2015 12:20:41 -0600
From: gmckinley@example.com
To: fakeaddress@example.com
Subject: Fwd: Bad email on order ack # 602278
Body: Description##Bad email address on order ack # 602278##
Service##ERP##
CI##APP_PAM_PRMS##
Staff##Greg McKinley##
Impact##Low##
Urgency##Low##

It was just the letter S as the email address.
Notified Kelsey.

This has been completed

---------- Forwarded message ----------
From: Gregory McKinley <gmckinley@example.com>
Date: Tue, Mar 31, 2015 at 12:19 PM
Subject: Bad email on order ack # 602278
To: Kelsey Crawford <kcrawford@example.com>


Hi Kelsey,
...
Please try again.

Thanks,
Greg
"""
    
    yield """
860 Move Log File
Sent: Mon, 21 Dec 2015 13:55 -0700
From: edi@exampleam.com
To: helpdesk@example.com
Subject: EDI 860 Move Log File
Body: See attached log
Impact##HIGH##
Urgency##HIGH##
Service##Office Services##
CI##APP_INF_PAM_EDI##
Description##860 Move Log File##
Staff##Matt Hanson##
"""

    yield """
Sent: Tue, 1 Jul 2014 16:32:41 +0200
From:example@example.com
To: fakeaddress@example.com
Subject: Re: Service Request #00292653 has been created
Body: Hello,

Je n'ai pas de nouvelles de ce ticket, et ça commence à urger.
Vous pouvez me tenir au courant ?

J'ai essayé d'ajouter une note sur la requête dans Take IT easy, mais ma
note n'a pas été enregistrée (le bouton "add" vide le champ, mais n'ajoute
pas la note)
[image: Inline images 1]

--
Boris Fakename
Chef de projet web
www.example.com


On 17 June 2014 11:22, example Take IT Easy <fakeaddress@example.com> wrote:

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
From: example@petzl.com
To: fakeaddress@petzl.com
Subject: Cognos Migration Incomplete
Body: Hello,

For C8 under domain PetzlAM and PetzlFR the migration looks incomplete ,
not all of my reports are under Accounting.  Under domain PetzlAM (Old) my
reports are there.
Is this what you would expect or should I be seeing under PetzlFR all of my
reports at this time?
'
Thanks,

*Dianne Anderson*
Senior Financial Accountant
*Petzl America*
tel 801.926.1571
toll free 877.807.3805 x7223
fax 801.926.1571
example@petzl.com
www.petzl.com
"""
