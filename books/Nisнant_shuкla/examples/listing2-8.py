import tensorflow as tf

x = tf.constant([[1., 2.]])
negMatrix = tf.negative(x)

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    result = sess.run(negMatrix)
print(result)
