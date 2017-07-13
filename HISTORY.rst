.. :changelog:

1.3.0
=====
Databmodel maintenance release. The main reason for this release was to clean
up the datamodel. This upgrade will changed the model and therefor will
trigger changes on the database if a new revision is made. I recommend to do
the upgrade as soon as possible, but it is not a must.

- Removed NM-Table to link printtemplates with items of a specific modul. This
  table was not needed is always empty. So it is removed now.

- Changed behaviour of the "printtemplates" attribute which is added
  dynamically to the printable items. This attribute now holds a list of
  printtemplates which are linked to the current item instead of a list
  of all available printtemplates.

1.2.5
=====

1.2.4
=====

1.2.3
=====

1.2.2
=====

1.2.1
=====

1.2
===

1.1
===
