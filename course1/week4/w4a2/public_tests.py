import numpy as np
from test_utils import single_test, multiple_test

         
def two_layer_model_test(target):
    np.random.seed(1)
    n_x = 10
    n_h = 4
    n_y = 1
    num_examples = 10
    num_iterations = 2
    layers_dims = (n_x, n_h, n_y)
    learning_rate = 0.0075
    X = np.random.randn(n_x, num_examples)
    Y = np.random.randn(1, num_examples)
    
    expected_parameters = {'W1': np.array([[ 0.01624965, -0.00610741, -0.00528734, -0.01072836,  0.008664  ,
                                 -0.02301103,  0.01745639, -0.00760949,  0.0031934 , -0.00248971],
                                [ 0.01462848, -0.02057904, -0.00326745, -0.00383625,  0.01138176,
                                 -0.01097596, -0.00171974, -0.00877601,  0.00043022,  0.00584423],
                                [-0.01098272,  0.01148209,  0.00902102,  0.00500958,  0.00900571,
                                 -0.00683188, -0.00123491, -0.00937164, -0.00267157,  0.00532808],
                                [-0.00693465, -0.00400047, -0.00684685, -0.00844447, -0.00670397,
                                 -0.00014731, -0.01113977,  0.00238846,  0.0165895 ,  0.00738212]]),
                         'b1': np.array([[ 1.10437111e-05],
                                [ 1.78437869e-05],
                                [ 3.74879549e-05],
                                [-4.42988824e-05]]),
                         'W2': np.array([[-0.00200283, -0.00888593, -0.00751122,  0.01688162]]),
                         'b2': np.array([[-0.00689018]])}
    expected_costs = [np.array(0.69315968)]
    
    expected_output = (expected_parameters, expected_costs)
    
    test_cases = [
        {
            "name":"datatype_check",
            "input": [X, Y, layers_dims, learning_rate, num_iterations],
            "expected": expected_output,
            "error":"Datatype mismatch."
        },
        {
            "name": "shape_check",
            "input": [X, Y, layers_dims, learning_rate, num_iterations],
            "expected": expected_output,
            "error": "Wrong shape"
        },
        {
            "name": "equation_output_check",
            "input": [X, Y, layers_dims, learning_rate, num_iterations],
            "expected": expected_output,
            "error": "Wrong output"
        }
    ]
    
    multiple_test(test_cases, target)
    
            
        
def L_layer_model_test(target):
    np.random.seed(1)
    n_x = 10 
    n_y = 1
    num_examples = 10
    num_iterations = 2
    layers_dims = (n_x, 5, 6 , n_y)
    learning_rate = 0.0075
    X = np.random.randn(n_x, num_examples)
    Y = np.array([1,1,1,1,0,0,0,1,1,0]).reshape(1,10)
    
    expected_parameters = {'W1': np.array([[ 0.51384638, -0.19333098, -0.16705238, -0.33923196,  0.273477  ,
         -0.72775498,  0.55170785, -0.24077478,  0.10082452, -0.07882423],
        [ 0.46227786, -0.65153639, -0.10192959, -0.12150984,  0.35855025,
         -0.34787253, -0.05455001, -0.27767163,  0.01337835,  0.1843845 ],
        [-0.34790478,  0.36200264,  0.28511245,  0.15868454,  0.284931  ,
         -0.21645471, -0.03877896, -0.29584578, -0.08480802,  0.16760667],
        [-0.21835973, -0.12531366, -0.21720823, -0.26764975, -0.21214946,
         -0.00438229, -0.35316347,  0.07432144,  0.52474685,  0.23453653],
        [-0.06060968, -0.28061463, -0.23624839,  0.53526844,  0.01597194,
         -0.20136496,  0.06021639,  0.66414167,  0.03804666,  0.19528599]]),
 'b1': np.array([[-2.16491028e-04],
        [ 1.50999130e-04],
        [ 8.71516045e-06],
        [ 5.57557615e-05],
        [-2.90746349e-05]]),
 'W2': np.array([[ 0.13428358, -0.15747685, -0.51095667, -0.15624083, -0.09342034],
        [ 0.26226685,  0.3751336 ,  0.41644174,  0.12779375,  0.39573817],
        [-0.33726917,  0.56041154,  0.22939257, -0.1333337 ,  0.21851314],
        [-0.03377599,  0.50617255,  0.67960046,  0.97726521, -0.62458844],
        [-0.64581803, -0.22559264,  0.0715349 ,  0.39173682,  0.14112904],
        [-0.9043503 , -0.13693179,  0.37026002,  0.10284282,  0.34076545]]),
 'b2': np.array([[ 1.80215514e-07],
        [-1.07935097e-04],
        [ 1.63081605e-04],
        [-3.51202008e-05],
        [-7.40012619e-05],
        [-4.43814901e-05]]),
 'W3': np.array([[-0.09079199, -0.08117381,  0.07667568,  0.16665535,  0.08029575,
          0.04805811]]),
 'b3': np.array([[0.0013201]])}
    expected_costs = [np.array(0.70723944)]
    
    expected_output = (expected_parameters, expected_costs)
    
    test_cases = [
        
        {
            "name": "equation_output_check",
            "input": [X, Y, layers_dims, learning_rate, num_iterations],
            "expected": expected_output,
            "error": "Wrong output"
        },
        {
            "name":"datatype_check",
            "input": [X, Y, layers_dims, learning_rate, num_iterations],
            "expected": expected_output,
            "error":"Datatype mismatch."
        },
        {
            "name": "shape_check",
            "input": [X, Y, layers_dims, learning_rate, num_iterations],
            "expected": expected_output,
            "error": "Wrong shape"
        }
    ]
    
    multiple_test(test_cases, target)