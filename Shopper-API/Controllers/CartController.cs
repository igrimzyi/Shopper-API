using Microsoft.AspNetCore.Mvc;
using ShopperAPI.Contracts.Cart;

namespace ShopperAPI.Controllers; 

[ApiController]
[Route("api/[controller]")]

public class CartController : ControllerBase  
{
    [HttpPost("/cart")]
    public IActionResult CreateCart(CreateCartRequest request)
    {  
        var Cart = new Cart(
            Guid.NewGuid(),
            request.CustomerId,
            request.CartId,
            request.Shoe
        );

        var response = new CartResponse(
            Cart.Id,
            Cart.CustomerId,
            Cart.CartId,
            Cart.Shoe
        );

        return CreatedAtAction(
            actionName: nameof(GetCart),
            routeValues: new { id = Cart.Id },
            value: response
        );
        //return Ok(response);
    }

    [HttpGet("{id:guid}")]
    public IActionResult GetCart(Guid id,UpsertCartRequest request)
    {
        return Ok(request);
    }

    [HttpDelete("{id:guid}")]
    public IActionResult DeleteCart(Guid id)
    {
        return Ok(id);
    }

}
