namespace Shopper-API.Contracts.Cart

    public record UpsertCartRequest(
    
        string CustomerId,
        string CartId,
        List<string> ProductIds
        
    )
