package grails3.example

class UrlMappings {

    static mappings = {
        "/api/search"(controller: "search", action: "search", method: "GET")
        "/api/signup"(controller: "user", action: "signUp", method: "POST")
        "/api/test"(controller: "test", action: "viewAccount", method: "GET")
        "/api/json"(controller: "test", action: "simplejson", method: "GET")


        "/"(view:"/index")
        "/**"(view:"/index")
    }
}
