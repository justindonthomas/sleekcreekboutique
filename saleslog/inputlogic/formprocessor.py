class FormProcessor(object):
    """
    Base form processor.
    """

    def __init__(self, user, postObject, FormType):
        """
        Receive a request.post and store cleaned data.

        user            request.user
        postObject      request.post
        FormType        Class of form to process.
        """
        self.user = user
        self.cleanedData = None
        f = FormType(postObject)
        if user.is_anonymous or not f.is_valid():
            self.cleanedData = None
        else:
            self.cleanedData = f.cleaned_data

