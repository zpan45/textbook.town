package grailsproject

class Profile {
    String displayName
    String contactMethod
    // Need an instance variable for profile photo

    // belongsTo is used to show ownership and cascade deletes if necessary
    static belongsTo = [account: UserAccount]

    static hasMany = [bids: Bid, textbooks: Textbook]

    static constraints = {
        bids nullable: true
        textbooks nullable: true
    }
}
