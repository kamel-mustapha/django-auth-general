# Versatile Authentication App

This **versatile and user-friendly authentication app** is designed for seamless integration into your applications. It offers a comprehensive suite of features, including:

- **Account Registration**: Easily allow users to create accounts.
- **Secure Login**: Ensure reliable and secure access to your platform.
- **Token Refresh**: Maintain session integrity with token renewal.
- **Password Reset**: Simplify password recovery for users.

**Perfect for general-purpose authentication needs**, this app strengthens your application's security while providing a smooth user experience.

---

## Required Environment Variables

To configure the app, ensure the following environment variables are set:

- `PROD=`
- `SECRET_KEY=`
- `EMAIL_HOST=`
- `EMAIL_HOST_USER=`
- `EMAIL_HOST_PASSWORD=`
- `COMPANY_NAME=`
- `ACTIVATION_REDIRECT_URL=`
- `SUPPORT_EMAIL=`
- `REDIRECTION_AFTER_ACTIVATION=`
- `APPLICATION_LOGIN_PAGE=`
- `RESET_PASSWORD_LINK=`
- `USER_TABLE_NAME=`

---

## Running the App with Docker Compose

You can deploy this authentication app quickly using the provided **Docker Compose** configuration:

```yaml
version: "3.8"
services:
  user:
    build: ./user
    restart: always
    ports:
      - 8085:8000
    volumes:
      - ./user/:/app/
    environment:
      - PROD=${PROD}
      - SECRET_KEY=${SECRET_KEY}
      - EMAIL_HOST=${EMAIL_HOST}
      - EMAIL_HOST_USER=${EMAIL_HOST_USER}
      - EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}
      - COMPANY_NAME=${COMPANY_NAME}
      - ACTIVATION_REDIRECT_URL=${ACTIVATION_REDIRECT_URL}
      - SUPPORT_EMAIL=${SUPPORT_EMAIL}
      - REDIRECTION_AFTER_ACTIVATION=${REDIRECTION_AFTER_ACTIVATION}
      - APPLICATION_LOGIN_PAGE=${APPLICATION_LOGIN_PAGE}
      - RESET_PASSWORD_LINK=${RESET_PASSWORD_LINK}
      - USER_TABLE_NAME=${USER_TABLE_NAME}
```
