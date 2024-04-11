def test_case():
    yield """
Sent: Tue, 27 Jan 2015 15:20:32 -0700
From: benm@example.com
To: takeiteasy@example.com
Subject: Did you fix my widget yet?
Body: Check out our new example Solutions website for a virtual tour!
*http://examplesolutions.com
<http://examplesolutions.com>*



*Ben Montgomery*CSS Manager


*example America*

2929 Decker lake Dr.
Salt Lake City, UT  84119
toll free *877-740-3827*
tel 801 926 1540 ext. 7240
fax 801 926 1501
BenM@example.com
    """
    
    yield """
Bad email address on order ack # 602278
Sent: Tue, 31 Mar 2015 12:20:41 -0600
From: gmckinley@example.com
To: takeiteasy@example.com
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
From: bstephan@example.com
To: takeiteasy@example.com
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


On 17 June 2014 11:22, example Take IT Easy <takeiteasy@example.com> wrote:

>  Hello,
>
> Service Request #00292653 has been created and assigned to the Service
...
> Thank you,
>
> Service Desk Team
>
"""