import grails3.example.Profile
import grails3.example.Role
import grails3.example.User
import grails3.example.UserRole

class BootStrap {

    def init = { servletContext ->
        def role = new Role(authority: 'ROLE_USER').save()
        def user = new User(username: 'test', password: '2212',
                            profile: new Profile(displayName: 'Philip', contactMethod: 'facebook')).save()
        UserRole.create(user, role, true)


    }
    def destroy = {
    }
}
