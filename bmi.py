while True:
    height = input('Write your height:')
    weight = input('Write your weight:')
    bmi = float(weight) / float(height) ** 2 * 10000
    BMI_TEXT = '[저체중-18.5-정상-23-과체중-25-비만-30-고도비만]'


    if bmi <= 18.5:
        level = '저체중'
    elif 18.5 <= bmi < 23:
        level = '정상'
    elif 23 <= bmi < 25:
        level = '과체중'
    elif 25 <= bmi < 30:
        level = '비만'
    else:
        level = '고도비만'
     
     
    # print screen

    print('{}\nYour BMI is {:.2f} \n당신은 {}입니다.'.format(BMI_TEXT, bmi, level))