from math import pi
import tensorflow as tf

mean = 0.0
sigma = 1.0
x = tf.constant([[1, 2]])

result = (tf.exp(tf.negative(tf.pow(x, 2) / (2 * tf.pow(sigma, 2) ))) *
 (1.0 / (sigma * tf.sqrt(2.0 * pi) )))

print(result)
