# from mail_templated import EmailMessage
#
#
# class ExamFeedbackEmail(EmailMessage):
#
#     def __init__(self, template_name=None, context={}, *args, **kwargs):
#         """
#         Initialize single templated email message (which can be sent to
#         multiple recipients).
#
#         When using with a user-specific message template for mass mailing,
#         create new EmailMessage object for each user. Think about this class
#         instance like about a single paper letter (you would not reuse it,
#         right?).
#
#         The class tries to provide interface as close to the standard Django
#         classes as possible.
#         |main_difference|
#
#         All parameters are optional and can be set at any time prior to calling
#         the :meth:`render()` and :meth:`send()` methods.
#
#         Note
#         ----
#
#         .. |args_note| replace:: The set of possible parameters is not limited
#             by the list below. Any additional parameters are passed to the
#             constructor of
#             :class:`EmailMultiAlternatives <django.core.mail.EmailMessage>`
#             class.
#
#         |args_note|
#
#         .. |template_name| replace:: The template name that extends
#             `mail_templated/base.tpl` with (optional) blocks ``{% subject %}``,
#             ``{% body %}`` and ``{% html %}``.
#
#         .. |context| replace:: A dictionary to be used as a context for
#             template rendering.
#
#         .. |from_email| replace:: The email address for the "From:" field.
#
#         .. |recipient_list| replace:: The recipient email addresses. Each
#             member of this list will see the other recipients in the "To:"
#             field of the email message.
#
#         .. |subject| replace:: Default message subject. Used if
#             ``{% subject %}`` block is empty or does not exist in the
#             specified email template.
#
#         .. |body| replace:: Default message body. Used if ``{% body %}``
#             block is empty or does not exist in the specified email template.
#
#         .. |render| replace:: If ``True``, render template and set ``subject``,
#             ``body`` and ``html`` properties immediately. Default is ``False``.
#
#         Arguments
#         ---------
#         template_name : str
#             |template_name|
#         context : dict
#             |context|
#         from_email : str
#             |from_email|
#         recipient_list : list
#             |recipient_list|
#
#         Keyword Arguments
#         -----------------
#         subject : str
#             |subject|
#         body : str
#             |body|
#         render : bool
#             |render|
#         clean : bool
#             If ``True``, remove any template specific properties from the
#             message object. This may be useful if you pass ``render=True``.
#             Default is ``False``.
#         """
#         self.template_name = template_name
#         self.context = context
#         subject = kwargs.pop('subject', None)
#         body = kwargs.pop('body', None)
#         render = kwargs.pop('render', False)
#         clean = kwargs.pop('clean', False)
#         self.template = None
#         self._is_rendered = False
#
#         super(EmailMessage, self).__init__(subject, body, *args, **kwargs)
#
#         if render:
#             self.render()
#         if clean:
#             self.clean()
