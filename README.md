# DjNRO

## Description
DjNRO is more than keeping eduroam.org updated with data. In essence it is a distributed management application.
It is distributed in the sense that information about each institution locations and services is kept up-to-date by each local eduroam administrator.
Keeping in pace with eduroam's federated nature, the implementation uses federated authentication/authorisation mechanisms, namely Shibboleth plus social media itegration.
The local institution eduroam administrators can become DjNRO admins. Local eduroam administrators register to the application via Shibboleth.
Once the accounts are acitvated, local eduroam admins can manage their eduroam locations, contact points and institution information.

## Installation Considerations
[![Documentation Status](https://readthedocs.org/projects/djnro/badge/?version=latest)](https://readthedocs.org/projects/djnro/?badge=latest)

You can find the installation instructions for Debian Wheezy (64)
with Django 1.4.x at [Djnro documentation](http://djnro.readthedocs.org).
If upgrading from a previous version bear in mind the changes introduced in Django 1.4.

## Contact

You can find more about Djnro or raise your issues at [GRNET Djnro
repository](https://code.grnet.gr/djnro), [GRNET Djnro Github repository](https://github.com/grnet/djnro), [Djnro mailing list](https://lists.grnet.gr/wws/info/djnro) or [GRNET Djnro minisite](http://djnro.grnet.gr/).

## LICENCE
Copyright © 2011-2015 Greek Research and Technology Network (GRNET S.A.)

Developed by Leonidas Poulopoulos (leopoul-at-noc-dot-grnet-dot-gr),
Zenon Mousmoulas (zmousm-at-noc-dot-grnet-dot-gr) and Stavros Kroustouris
(staurosk-at-noc-dot-grnet-dot-gr), GRNET NOC

Contributions by Jamie Curtis, REANNZ

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
SOFTWARE.
