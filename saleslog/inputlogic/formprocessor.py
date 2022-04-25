class FormProcessor(object):
    """
    Base form processor.
    """

    def __init__(self, user, postObject, FormType):
        """
        Receive a request.post and store cleaned data.

        Constructor args:

        user            request.user
        postObject      request.post
        FormType        Class of form to process.

        Members:

        user            request.user
        cleanedData     Cleaned data from form.
        """
        self.user = user
        self.cleanedData = None
        f = FormType(postObject)
        if user.is_anonymous or not f.is_valid():
            print(f.errors)
            self.cleanedData = None
            print("Form invalid")
        else:
            print("Form valid")
            self.cleanedData = f.cleaned_data

