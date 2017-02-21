package grails3.example

class Bid {
    int ceiling

    static belongsTo = [auction: Auction, bidder: Profile]

    static constraints = {
        auction nullable: false
        bidder nullable: false
        ceiling nullable: false
    }
}