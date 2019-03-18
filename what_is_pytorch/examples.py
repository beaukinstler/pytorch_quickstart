import app
import torch

def basic_examples():
    app.p("EXAMPLES")
    app.p("Construct a 5x3 matrix, uninitialized:")
    x = torch.empty(5, 3)
    print(x)

    app.p("Construct a randomly initialized matrix: ")
    x = torch.empty(5, 3)
    print(x)

    app.p("Construct a matrix filled zeros and of dtype long:")
    x = torch.zeros(5, 3, dtype=torch.long)
    print(x)


    app.p("Construct a tensor directly from data:")
    x = torch.tensor([5.5, 3])
    print(x)

    app.p("""or create a tensor based on an existing tensor. 
         These methods will reuse properties of the input 
         tensor, e.g. dtype, unless new values are provided by user""")
    x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
    print(x)
    x = torch.randn_like(x, dtype=torch.float)    # override dtype!
    print(x)                                      # result has the same size

    app.p("Get its size:")
    print(x.size())  # returns a tuple
    app.p("Size object that's returned is a tuple")
    tup = x.size()
    print(tup)
    print(tup[-1])
    print(tup.count(5))

def operation_examples():
    app.p("OPERATIONS")
    
    app.p("addition")
    x = torch.tensor([10, 4])
    print(type(x))
    print(x)
    y = torch.rand(5, 3)
    print(type(y))
    print(y)
    x = x.new_ones(5, 3, dtype=torch.double)
    print(x)
    x = torch.randn_like(x, dtype=torch.float)
    y = torch.rand(5, 3)
    print(x)
    print(y)
    print(x + y)

def view_examples():
    app.p("VIEWS")

    app.p("""Views change the shape, but share underlying objects
         Like a pointer would reference the shared memory""")
    
    app.p("create a torch.Tensor called x, 4 ")
    x = torch.randn(4, 4)
    print(x)
    
    app.p("share the data, but view it as one array 16 items")
    y = x.view(16)
    print("y = x.view(16); print(y)")
    print(y)    

    app.p("Print column 2 from x with print(x[:, 1])")
    print(x[:, 1])

    app.p("y doesn't have a column. Must use print(y[:]) ")
    print(y[:])

    app.p("Print column 2, up to row 2 from x with print(x[:2, 1])")
    print(x[:2, 1])

def item_examples():
    app.p("If you have a one element tensor, use .item() to get the value as a Python number")
    x = torch.randn(1)
    print(x)
    print(x.item())


if __name__ == '__main__':
    pass

    
