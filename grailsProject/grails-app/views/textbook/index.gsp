<%--
  Created by IntelliJ IDEA.
  User: piercesaly
  Date: 2017-02-15
  Time: 7:08 PM
--%>

<%@ page contentType="text/html;charset=UTF-8" %>

<!DOCTYPE html>
<html>
<head>
    <meta name="layout" content="main"/>
    <title>Index</title>
</head>
<body>
<g:form controller="textbook">
    <label>Email: </label>
    <g:textField name="emailAddress"/><br/>
    <label>Password: </label>
    <g:textField name="password"/><br/>
    <label>Display Name: </label>
    <g:textField name="displayName"/><br/>
    <label>Contact Method: </label>
    <g:textField name="contactMethod"/><br/>
    <g:actionSubmit value="Create" action="createAccount"/>
</g:form>
</body>
</html>