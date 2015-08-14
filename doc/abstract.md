# Introducing BIBCAT - a BIBFRAME Catalog

The Library of Congress efforts to replace MARC21 with a new linked-data 
vocabulary called BIBFRAME is generating much discussion in the library 
community. A new open-source library catalog 
and digital repository called BIBCAT - a project funded by the Library of 
Congress - demonstrates what a new linked-data catalog could look 
like for libraries and with a prototype available at http://bibcat.org/. 
 
## Introduction
The library's catalog, usually the core of what is called the library's
integrated library systems and now being marketed as "library services
platform" (Breeding 2012), touches most areas of the library's
operations, collections, and public services. The functionality needed
to support acquisition and circulation work-flows - not mention the
increasingly complex electronic resource management for journals and
e-books - traditionally requires these large enterprise software systems
to include all this functionality into large monolithic "black-boxes".

In the Spring 2014 issue of Reference and User Services Quarterly, Diane
Cmor and Rory Litwin argue if libraries should keep the traditional
library OPAC in favor of discovery systems or what Athena Hoeppner
describes as "web-scale discovery services" (Hoeppner 2012). Cmor's
position, that because library patrons prefer to using discovery systems
to the traditional OPAC for finding the library's materials, the added
costs of maintaining two separate systems argue in favor of dropping or
eliminating the traditional library ILS/OPAC or catalog. Litwin's
counter-argument for retaining the traditional catalog revolve around
the catalog's utility for advanced searching by scholars and experts is
better for their specific information needs than the current crop of
discovery systems that focus on the general undergraduate at a academic
library.(Cmor and Litwin 2014)

Although that might not have been the intentions of either Cmor or
Litwin in their debate on retiring the library catalog, there is another
alternative to what either of them suggest for library catalog. Instead
of purchasing a commercial discovery system or deploying one of the
open-source discovery layer alternatives, libraries should consider if
their rate-of-return on their technology investment for resource
discovery would be better spent through online adverting of their
collections on the major commercial general search like Google or
Microsoft Bing. This radical approach has already been investigated by
libraries as Utrecht University Library, where their student patrons
start their search 83% of the time from a search engine with under 1%
using a online databases and the library website. (Kortekaas 2012)

With such library luminaries as Roy Tennent calling for the demotion of
the library catalog by encouraging libraries to "Take that anachronistic
library catalog and turn it back into what it really only ever was - an
inventory control system." (Tennent 2014) or as Diane Cmor says
"Obviously, we still need back-end catalogs (or the equivalent) to feed
our holdings into our discovery systems, but the user interface is no
longer necessary." (Cmor and Litwin 2014) Lacking from these analysis is
that poor user interface for backend enterprise systems, even stripped
down to bare functionality as envisioned by Tennent and Cmor, have real
and significant costs that are borne by library staff and administration
when trying to accomplish their workflow in the library.

## Simplifying and De-coupling Library Technology

Inspired by John Hegel III's and John Seely Brown's early conception a
pull platforms, the Tutt Library has embarked on approach for library
catalog software development that emphasis emergent design, loosely
coupled, people focused with incremental cycles that provide immediate
feedback from the end users of these services (Hegal II and Brown 2008).
The current technical infrastructure includes open-source projects like
Fedora Commons and Elastic search for RDF and datastream management and
search functionality while supporting existing MARC21 works and newer
command-line and web-based tools for manipulating RDF graphs of BIBFRAME
and schema.org vocabularies. This infrastructure is illustrated below:

This simplifying process will eventually center around using Fedora 4 as
both a replacement for the MARC-based ILS through direct datastream
management of the exported MARC records at Tutt Library while also
directly supporting the ingestion and use of BIBFRAME and Schema.org
triples for Tutt Library's creative works. To maximize utility and
leverage the wide adoption of JSON, JSON linked data representations of
these creative works are published and consumed between the front-end
web applications, Fedora, and Elastic Search using JSON-LD
serializations from Fedora.

## BIBFRAME - Library of Congress's MARC21 Replacement
BIBFRAME, short for Bibliographic Framework Initiative, refers to both 
the vocabulary as well as the communities and organizations that 
understand the importance of bibliographic data to libraries and other 
cultural heritage institutions. BIBFRAME as described from the Library 
of Congress website, is

    Initiated by the Library of Congress, BIBFRAME provides a foundation 
    for the future of bibliographic description, both on the web, and in 
    the broader networked world…In addition to being a replacement for MARC, 
    BIBFRAME serves as a general model for expressing and connecting 
    bibliographic data. A major focus of the initiative will be to determine 
    a transition path for the MARC 21 formats while preserving a robust 
    data exchange that has supported resource sharing and cataloging cost 
    savings in recent decades.  

As one of the first adopters, Jeremy Nelson 

## BIBCAT and the Catalog Pull Platform

## Reimagining the Colorado College Library's TIGER Catalog and Website


## References

http://www.loc.gov/bibframe/
