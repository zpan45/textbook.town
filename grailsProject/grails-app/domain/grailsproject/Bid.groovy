package grailsproject

class Bid {
    int ceiling

    static belongsTo = [auction: Auction, bidder: Profile]

    static constraints = {
    }
}
