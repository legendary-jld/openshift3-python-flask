from flask import Blueprint, session


errorhandling = Blueprint('errorhandling', __name__, template_folder="templates/errors")


class Error:
    def __init__(self, exception, code=None, title="", message=""):
        self.exception = exception
        self.code = code
        self.title = title
        self.message = message

        if self.code in (400,401,403,404,405,408):
            self.capture_error()
        elif self.code == 404:
            self.capture_404()

    def capture_error(self):
        # Save to database or log file or print to console, etc
        pass

    def capture_404(self):
        # 404 logged a little differently
        pass



@errorhandling.app_errorhandler(400)
def bad_request_400(exception):
    error = Error(exception, 400, "Bad Request", "An error occured during the request, please try again.")
    return render_template("base_error.html", error=error)


@errorhandling.app_errorhandler(401)
def unauthorized_401(exception):
    error = Error(exception, 401, "Unauthorized", "Unauthorized to access this resource, please make sure you have logged in.")
    return render_template("base_error.html", error=error)


@errorhandling.app_errorhandler(403)
def forbidden_403(exception):
    error = Error(exception, 403, "Forbidden", "Access to this resource is forbidden, or you have not yet been granted the rights.")
    return render_template("base_error.html", error=error)


@errorhandling.app_errorhandler(404)
def not_found_404(exception):
    error = Error(exception, 404, "Not Found", "The resource you're looking for could not be found or is no longer available.")
    return render_template("base_error.html", error=error)


@errorhandling.app_errorhandler(405)
def method_not_allowed_405(exception):
    error = Error(exception, 405, "Method Not Allowed", "That method is not permitted on this resource.")
    return render_template("base_error.html", error=error)


@errorhandling.app_errorhandler(408)
def request_timeout_408(exception):
    error = Error(exception, 408, "Request Timeout", "A timeout occured while trying to access this resource.")
    return render_template("base_error.html", error=error)


@errorhandling.app_errorhandler(500)
def server_error_500(exception):
    error = Error(exception, 500, "Server Error", "A timeout occured while trying to access this resource.")
    return render_template("base_error.html", error=error)


@errorhandling.app_errorhandler(Exception)
def unhandled_exception(exception):
    error = Error(exception, None, "Server Error", "An unknown error has occured for this resource.")
    return render_template("base_error.html", error=error)
