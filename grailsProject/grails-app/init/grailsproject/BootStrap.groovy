package grailsproject

class BootStrap {

    // The contents of this method get executed when the program starts running
    def init = { servletContext ->
        new UserAccount(emailAddress: "bleh@me", password: "123456", profile: new Profile(displayName: "Bleh", contactMethod: "facebook")).save()
        def p = Profile.find{displayName == "Bleh"}
        print(p.getAccount().getPassword())
    }
    def destroy = {
    }
}
