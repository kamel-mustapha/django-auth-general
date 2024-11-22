from django.conf import settings

def register_template(username, link, expires_in, support_email):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Activate Your Account</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
            }}
            .header {{
                text-align: center;
                padding: 20px 0;
            }}
            .header h1 {{
                color: #333333;
                margin: 0;
            }}
            .content {{
                font-size: 16px;
                color: #555555;
                line-height: 1.5;
            }}
            .button-container {{
                text-align: center;
                margin: 20px 0;
            }}
            .button {{
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                color: #ffffff;
                background-color: #007bff;
                text-decoration: none;
                border-radius: 5px;
            }}
            .footer {{
                text-align: center;
                font-size: 14px;
                color: #aaaaaa;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <h1>Activate Your Account</h1>
            </div>
            <div class="content">
                <p>Hi {0},</p>
                <p>Thank you for signing up with {1}! To get started, please activate your account by clicking the button below:</p>
                <div class="button-container">
                    <a href="{2}" class="button">Activate My Account</a>
                </div>
                <p>If the button above doesn't work, copy and paste the following link into your browser:</p>
                <p>{2}</p>
                <p>This link will expire in {3}, so be sure to activate your account soon.</p>
            </div>
            <div class="footer">
                <p>Need help? Contact our support team at <a href="mailto:{4}">{4}</a>.</p>
                <p>&copy; 2024 {1}. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
""".format(username, settings.COMPANY_NAME, link, expires_in, support_email)


def invalid_token():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Invalid Token</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                text-align: center;
                background-color: #ffffff;
                padding: 20px 40px;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .container h1 {
                color: #dc3545;
                font-size: 24px;
                margin-bottom: 10px;
            }
            .container p {
                font-size: 16px;
                color: #555555;
                margin-bottom: 20px;
            }
            .container a {
                text-decoration: none;
                color: #ffffff;
                background-color: #007bff;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
            }
            .container a:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Invalid or Expired Token</h1>
            <p>We're sorry, but the token you provided is invalid or has expired.</p>
        </div>
    </body>
    </html>
"""


def activation_success():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Account Activated</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                text-align: center;
                background-color: #ffffff;
                padding: 20px 40px;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .container h1 {{
                color: #28a745;
                font-size: 24px;
                margin-bottom: 10px;
            }}
            .container p {{
                font-size: 16px;
                color: #555555;
                margin-bottom: 20px;
            }}
            .container a {{
                text-decoration: none;
                color: #ffffff;
                background-color: #007bff;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
            }}
            .container a:hover {{
                background-color: #0056b3;
            }}
        </style>
        <script>
            // Redirect after 10 seconds
            setTimeout(function() {{
                window.location.href = '{0}'; 
            }}, 10000);
        </script>
    </head>
    <body>
        <div class="container">
            <h1>Account Activated</h1>
            <p>Your account has been successfully activated! You will be redirected shortly.</p>
            <p>If you are not redirected, <a href="{0}">click here</a>.</p> <!-- Replace with your dashboard URL -->
        </div>
    </body>
    </html>
""".format(settings.REDIRECTION_AFTER_ACTIVATION)

def account_already_activated():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Account Already Activated</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                text-align: center;
                background-color: #ffffff;
                padding: 20px 40px;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .container h1 {{
                color: #ffc107;
                font-size: 24px;
                margin-bottom: 10px;
            }}
            .container p {{
                font-size: 16px;
                color: #555555;
                margin-bottom: 20px;
            }}
            .container a {{
                text-decoration: none;
                color: #ffffff;
                background-color: #007bff;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
            }}
            .container a:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Account Already Activated</h1>
            <p>Your account is already active. You can now proceed to log in.</p>
            <a href="{0}">Go to Login</a>
        </div>
    </body>
    </html>
""".format(settings.APPLICATION_LOGIN_PAGE)


def reset_password_link(link):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reset Password</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                text-align: center;
                background-color: #ffffff;
                padding: 20px 40px;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 400px;
            }}
            .container h1 {{
                color: #007bff;
                font-size: 24px;
                margin-bottom: 20px;
            }}
            .container p {{
                font-size: 16px;
                color: #555555;
                margin-bottom: 20px;
            }}
            .container a {{
                text-decoration: none;
                color: #ffffff;
                background-color: #007bff;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
            }}
            .container a:hover {{
                background-color: #0056b3;
            }}
            .container .note {{
                font-size: 14px;
                color: #555555;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Reset Your Password</h1>
            <p>We received a request to reset your password. If you made this request, please click the link below to reset your password:</p>
            <a href="{0}" target="_blank">Reset Password</a> 
            <p class="note">If you didn’t request a password reset, please ignore this email.</p>
        </div>
    </body>
    </html>
""".format(link)


def reset_password_success():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Changed Successfully</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                text-align: center;
                background-color: #ffffff;
                padding: 20px 40px;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 400px;
            }}
            .container h1 {{
                color: #28a745;
                font-size: 24px;
                margin-bottom: 20px;
            }}
            .container p {{
                font-size: 16px;
                color: #555555;
                margin-bottom: 20px;
            }}
            .container a {{
                text-decoration: none;
                color: #ffffff;
                background-color: #007bff;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
            }}
            .container a:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Password Changed Successfully</h1>
            <p>Your password has been successfully changed. You can now log in with your new password.</p>
            <a href="{0}">Go to Login</a>
        </div>
    </body>
    </html>
""".format(settings.APPLICATION_LOGIN_PAGE)