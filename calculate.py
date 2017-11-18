#Calculate prior probability from the given question
store_c_l = {}
p0_h1 = 0.1
p0_h2 = 0.2
p0_h3 = 0.4
p0_h4 = 0.2
p0_h5 = 0.1

p_c_1 = 1
p_c_2 = 0.75
p_c_3 = 0.5
p_c_4 = 0.25
p_c_5 = 0

p_l_1 = 0
p_l_2 = 0.25
p_l_3 = 0.5
p_l_4 = 0.75
p_l_5 = 1
#calculate probability of getting an obeservation without any observations
flavour = "c"

p0_q1_c = p0_h1 * p_c_1 + p0_h2 * p_c_2 + p0_h3 * p_c_3 + p0_h4 * p_c_4 + 0
p0_q1_l = p0_h1 * p_l_1 + p0_h2 * p_l_2 + p0_h3 * p_l_3 + p0_h4 * p_l_4 + p0_h5 * p_l_5
input_string = "CLLCCLLLCCL"
#input_string = "C"
i = 1

for letter in input_string:

    if input_string == '':
        exec ("%s = %d" % ("p" + str(i) + "_q" + str(i + 1) + "_c", 0))
        posterior_prob = eval("p" + str(i) + "_q" + str(i + 1) + "_c")
        for j in range(1, 6):
            prob_previous_hypothesis = eval("p" + str(i - 1) + "_h" + str(j))
            prob_previous_observation = eval("p" + str(i - 1) + "_q" + str(i) + "_c")
            prob_hypothesis = "p" + str(i) + "_h" + str(j)
            exec ("%s = %f" % (
            prob_hypothesis, (eval("p_c_" + str(j)) * prob_previous_hypothesis) / prob_previous_observation))
            # prob_hypothesis =  (eval("p_c_"+str(j)) * prob_previous_hypothesis) / prob_previous_observation
            posterior_prob = posterior_prob + eval("p_c_" + str(j)) * eval(prob_hypothesis)
        print posterior_prob
        exec ("%s = %f" % ("p" + str(i) + "_q" + str(i + 1) + "_c", posterior_prob))
        exec ("%s = %f" % ("p" + str(i) + "_q" + str(i + 1) + "_l", 1 - posterior_prob))
        i = i + 1
        print "Final output probability for c is "+str(posterior_prob)
        print "Final output probability for l is "+str(1- posterior_prob)

    elif letter == "C":
    #posterior_prob = "p"+str(i)+"_q"+str(i+1)+"_c"
        exec("%s = %d" %("p"+str(i)+"_q"+str(i+1)+"_c",0))
        posterior_prob = eval("p"+str(i)+"_q"+str(i+1)+"_c")
        for j in range(1,6):
            prob_previous_hypothesis = eval("p"+str(i-1)+"_h"+str(j))
            prob_previous_observation = eval("p"+str(i-1)+"_q"+str(i)+"_c")
            prob_hypothesis = "p"+str(i)+"_h"+str(j)
            exec ("%s = %f" % (prob_hypothesis, (eval("p_c_"+str(j)) * prob_previous_hypothesis) / prob_previous_observation))
            #prob_hypothesis =  (eval("p_c_"+str(j)) * prob_previous_hypothesis) / prob_previous_observation
            posterior_prob = posterior_prob + eval("p_c_"+str(j)) * eval(prob_hypothesis)
        #print posterior_prob
        exec ("%s = %f" % ("p"+str(i)+"_q"+str(i+1)+"_c", posterior_prob))
        exec ("%s = %f" % ("p" + str(i) + "_q" + str(i + 1) + "_l", 1- posterior_prob))
        i = i + 1
        print "Final output probability for c is " + str(posterior_prob)
        print "Final output probability for l is " + str(1 - posterior_prob)
    elif letter == "L":
        exec ("%s = %d" % ("p" + str(i) + "_q" + str(i + 1) + "_l", 0))
        posterior_prob = eval("p" + str(i) + "_q" + str(i + 1) + "_l")
        for j in range(1, 6):
            prob_previous_hypothesis = eval("p" + str(i - 1) + "_h" + str(j))
            prob_previous_observation = eval("p" + str(i - 1) + "_q" + str(i) + "_l")
            prob_hypothesis = "p" + str(i) + "_h" + str(j)
            exec ("%s = %f" % (
            prob_hypothesis, (eval("p_l_" + str(j)) * prob_previous_hypothesis) / prob_previous_observation))
            # prob_hypothesis =  (eval("p_c_"+str(j)) * prob_previous_hypothesis) / prob_previous_observation
            posterior_prob = posterior_prob + eval("p_l_" + str(j)) * eval(prob_hypothesis)
        #print posterior_prob
        exec ("%s = %f" % ("p" + str(i) + "_q" + str(i + 1) + "_l", posterior_prob))
        exec ("%s = %f" % ("p" + str(i) + "_q" + str(i + 1) + "_c", 1 - posterior_prob))
        i = i + 1
        print "Final output probability for c is " + str(posterior_prob)
        print "Final output probability for l is " + str(1 - posterior_prob)

# exec ("%s = %d" % ("p" + str(i) + "_q" + str(i + 1) + "_c", 0))
# posterior_prob = eval("p" + str(i) + "_q" + str(i + 1) + "_c")
# for j in range(1, 6):
#     prob_previous_hypothesis = eval("p" + str(i - 1) + "_h" + str(j))
#     prob_previous_observation = eval("p" + str(i - 1) + "_q" + str(i) + "_c")
#     prob_hypothesis = "p" + str(i) + "_h" + str(j)
#     exec ("%s = %f" % (
#     prob_hypothesis, (eval("p_c_" + str(j)) * prob_previous_hypothesis) / prob_previous_observation))
#     # prob_hypothesis =  (eval("p_c_"+str(j)) * prob_previous_hypothesis) / prob_previous_observation
#     posterior_prob = posterior_prob + eval("p_c_" + str(j)) * eval(prob_hypothesis)
# print posterior_prob
# exec ("%s = %f" % ("p" + str(i) + "_q" + str(i + 1) + "_c", posterior_prob))
# exec ("%s = %f" % ("p" + str(i) + "_q" + str(i + 1) + "_l", 1 - posterior_prob))
# i = i + 1
# print "Final output probability for c is "+str(posterior_prob)
# print "Final output probability for l is "+str(1- posterior_prob)





            



