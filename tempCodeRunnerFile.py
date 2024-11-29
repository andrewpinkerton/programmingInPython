    t.color(r, g, b)
    
    t2.color(r, g, b)
    
    t.forward(count)
    
    t2.right(90)
    
    t2.forward(count)
    
    t.left(200)
    
    count += 1
    
    r = (r + 1) % 256
    
    g = (g + 2) % 256
    
    b = (b + 3) % 256