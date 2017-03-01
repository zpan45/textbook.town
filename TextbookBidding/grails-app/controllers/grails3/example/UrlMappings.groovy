package grails3.example

class UrlMappings {

    static mappings = {
        "/api/search"(controller: "search", action: "search", method: "GET")
        "/api/signup"(controller: "user", action: "signUp", method: "POST")
        "/api/test"(controller: "test", action: "viewAccount", method: "GET")
        "/api/json"(controller: "test", action: "simplejson", method: "GET")
        "/api/add"(controller: "textbook", action: "simpleAdd", method: "POST")
        "/api/imageFile"(controller: "file", action: "upload", method: "POST")


        "/"(view:"/index")
        "/**"(view:"/index")
    }
}
