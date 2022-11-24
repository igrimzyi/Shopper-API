namespace ShopperAPI.Models; 

public class Cart
{
    public Guid Id { get;  }
    public string CustomerId { get; }
    public string CartId { get; }
    public List<string> Shoe { get; }
}

public Cart(
    Guid id,
    string customerId,
    string cartId,
    List<string> shoe
)
{
    Id = id;
    CustomerId = customerId;
    CartId = cartId;
    Shoe = shoe;
}
