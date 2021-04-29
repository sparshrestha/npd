{% extends "mail_templated/base.tpl" %}
{% load i18n %}

{% block subject %}
  {% blocktrans %}EXAM REPORT!!{% endblocktrans %}
{% endblock %}

{% block html %}
  <p>Mr/Ms {{ student.student_name }}</p>
  <p>Please find your Report below.</p>
  <h1>Total Marks: {{ marks.final_marks }}.</h1>
  <br>
  <p>Regards</p>
  <p>OMR TEAM</p>
{% endblock html %}
