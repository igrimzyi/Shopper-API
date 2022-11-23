namespace Shopper-API.Contracts.Cart

    public record CreateCartRequest(
    
        string CustomerId,
        string CartId,
        List<string> ProductIds
        
    )
