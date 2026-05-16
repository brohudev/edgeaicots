- https://docs.micropython.org - start here.
     - micropython.mem_info() 
     - micropython.stack_use()
- https://micropython-ulab.readthedocs.io - this is the numpy equivalent for mp, will be used to create model weights and biases and so on.
- python random / urandom docs. 




---


Before each layer of the project, ask yourself:

Can you implement a 2-layer MLP forward pass using only ulab.numpy.dot() and an activation function you write yourself? If yes, you have your inference engine.

Can you write struct.pack('f', x), flip bit 23 (the LSB of the float mantissa), and unpack it back — knowing why that specific bit matters? If yes, you can write a meaningful SEU simulator.

Can you implement CRC-32 from the Wikipedia polynomial table without looking at any Python CRC library? If yes, you have your detection layer.

Can you read two bytes from the INA219 over machine.I2C and convert them to milliwatts using the register map formula? If yes, you can measure power overhead.

