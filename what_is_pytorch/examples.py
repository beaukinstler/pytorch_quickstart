from what_is_pytorch import *

def examples():
    # p("EXAMPLES")
    # p("Construct a 5x3 matrix, uninitialized:")
    # x = torch.empty(5, 3)
    # print(x)

    # p("Construct a randomly initialized matrix: ")
    # x = torch.empty(5, 3)
    # print(x)

    # p("Construct a matrix filled zeros and of dtype long:")
    # x = torch.zeros(5, 3, dtype=torch.long)
    # print(x)


    p("Construct a tensor directly from data:")
    x = torch.tensor([5.5, 3])
    print(x)

    p("""or create a tensor based on an existing tensor. 
         These methods will reuse properties of the input 
         tensor, e.g. dtype, unless new values are provided by user""")
    x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
    print(x)
    x = torch.randn_like(x, dtype=torch.float)    # override dtype!
    print(x)                                      # result has the same size

if __name__ == '__main__':
    examples()