# coding: utf-8
import tkinter as tk

meta_data={}

'''
规则

要的：没有电子版&&文件名中不包括测井的关键字&&四大件中为1的&&掏的数量小于等于5 

不要的：四大件中为2的+(有电子版&&文件名中不包括测井的关键字&&掏的数量大于5 ) 

全掏：掏的数量＞5，电子版数量为0

一本不要，掏的数量为0


'''

from selenium import webdriver
import time
import pandas as pd
_301='中、盘、盘、田、庄、岭试、原、砖、宁排、宁、沿、城、元东侧、元东、东、城、环、红、坊、华、樊、樊东、樊北、樊西、谭、华、樊、定庆、定、G、盐、苏、榆、G、盐、新、耿、高、玄、大、张、演、乌、升、安、庆、柴、碾、白、庙、苗、洼、天、'
_301_list=_301.split('、')
_209='罗、路、北、杨、招、黄、旗、贺、镰、塞、董、木、摆、于、化、元西、元东、元、马、真、岭、里、冯、蛟、镇、山、胡、西'
_209_list=_209.split('、')
_302='洪、岭平、岭试、红（宁夏）、金（宁夏）、悦、白、西、镇参、镇探、镇、环、演、元、木、合、固、龙、陇、泾、南、庄、镇川、泾参、定、泉、靖注、靖平、靖、大东、新东、东、大南、大、马坊、马探、马中、马深、马、新王、王平、王、胡、葫、吴、定、化、张、冯、真、石、楼、浦、淳探、旬探、宁探、桃、定探、宜探、红、艾、召探、召、富、富探、板、正、延深、跃参、新跃、跃枣、枣深、鱼、青、麒、麒参、牛、米、榆、坊、绥、碾、丹、摆、高、于探、新于、于、余深、旗、玄、铺、林、姬、砖、盟、苏参、苏、神、鄂、洲、郎、乐、谭、宝、洼、杨、里、剖、池、山、油兔、兔东、兔西、海、安深、安参、盘探、图、图东、银参、毕探、色、惠、鸳探、鸳参、黄、黄深、黄试、上、呼参、布、亥、锡、巴参、墩、吉参、吉、白西、芦参、苦深、苦东、羊、芨、刀、鸡、花、普、团、郭、曙、胜、碎探、杨探、周、北台、台、沙、沙坝、雨、雨东、雨中、徐、积参、黑中、罗、金（陕西）、金评、长、刘、刘庆、惠探、发、发东、发参、古、候、临深、临探、红、伊深、伊、李、李华、新盐、盐、新、耿、宁、任、蔡、桥、乔、樊、镰、梁、天深、天参、天、子、安陕参、陕钾、陕（1-187）、陕（188-255）、沿、柳、王评、红评、坪注、坪检、太、统、补、应、双、莲、原、井、学、洛、崔、老、理、资、浅、平、渭深、横、志、志参、杂井剖面、午、庙、蛟、永参、永、薛、宝、ZJ、AP、ZP、L、Z、DP、A、AJ、HP、XP、EY、中（97-311）、南、华、中（1-96）、城、庆、庆深、阳、北、南（1-4）、塞平、塞检、塞、城（7-15）'
_302_list=_302.split('、')


def calc_room(index_No,well_name):
    room_number=''
 
    #     '''
    #     304号
    #     18091-22987
    #     '''
    if (18091<=index_No)&(index_No<=22987):
        room_number='304'
    #     '''
    #     303号
    #     22988-27792

    #     '''
    elif (22988<=index_No)&(index_No<=27792):
        room_number='303'
    #     '''
    #     27793-32469
    #     209号
    #     '''
    elif (27793<=index_No)&(index_No<=32469):
        room_number='209'
    
    #     '''
    #     205号
    #     32470-37183
    #     '''
    elif (32470<=index_No)&(index_No<=37183):
        room_number='205'
    #     '''
    #     207号
    #     37184-44315
    #     '''
    elif (37184<=index_No)&(index_No<=44315):
        room_number='207'
    #     '''
    #     208号
    #     44316-52081
    #     '''
    elif (44316<=index_No)&(index_No<=52081):
        room_number='208'
    
    #     '''
    #     201	
    #     52082-61469
    #     '''
    elif (52082<=index_No)&(index_No<=61469):
        room_number='201'
    #     204号
    #     61470-69554
    elif (61470<=index_No)&(index_No<=69554):
        room_number='204'
    #     206号
    #     69555-80633
    elif (69555<=index_No)&(index_No<=80633):
        room_number='206'
    
    
        
    #0-18090（探井、评价井）
    elif index_No<18090:
        
        for well_ in _301_list:
            if (well_name.find(well_)>-1):
                room_number='301'
                break
        for well_ in _209_list:
            if (well_name.find(well_)>-1):
                room_number='209'
                break    
            
        for well_ in _302_list:
            if (well_name.find(well_)>-1):
                room_number='302'
                break    
               
    return room_number

def click_func():
    print('请稍等.....')

    #浏览器发起请求
    driver=webdriver.Chrome()
    login_url='http://10.78.7.51/common/Main.htm'
    driver.get(login_url)
    #模拟登录
    driver.execute_script("input_=document.getElementById('txtAccount');input_.value='liudong'")
    driver.execute_script("input_=document.getElementById('txtPassword');input_.value='liudong123'")
    driver.execute_script("rdlISSINGLE_1=document.getElementById('rdlISSINGLE_1')")
    driver.execute_script("rdlISSINGLE_1.checked='checked'")
    driver.execute_script("rdlISSINGLE_0=document.getElementById('rdlISSINGLE_0')")
    driver.execute_script("rdlISSINGLE_0.checked=''")
    btnLogon=driver.find_element_by_id('btnLogon')
    btnLogon.click()
    #转到搜索页
    search_url='http://10.78.7.51/DocumentRecord/SearchDocument.aspx'
    driver.get(search_url)
    
    test_well_list=['VSP','磁定位','地层倾角','电测','测井','水泥','校深']
    finished_picture_flag_list=['综合录井图','完井总结图','录井综合图']
    oil_experiment_flag_list=['试油','试油总结','试气总结报告','试油地质总结']
    finished_report_flag_list=['完井报告','完井总结报告','录井完井报告']
    core_analysis_flag_list=['岩心分析','岩芯分析']

    #借阅表
    borrow_table=pd.read_csv('未借阅.csv',encoding='gbk')
    borrow_table_copy=pd.DataFrame(columns=borrow_table.columns,index=range(0,200))
    print('登录成功..')
    print('开始下载资料..')

    for index_ in borrow_table.index:

        #一次查200口井
        #if(index_>500):
            #break


        #井信息
        borrow_info=borrow_table.ix[index_]
        #当前井号
        borrow_well=borrow_info['井号']
        
        if index_==0:
            first_well_name=borrow_well
        #是否要四大件
        finished_picture=not (borrow_info['录井图']-1)
        oil_experiment=not borrow_info['试油总结']-1
        finished_report=not borrow_info['完井报告']-1
        core_analysis=not borrow_info['岩心分析']-1

        #表单填写和发起搜索
        driver.execute_script("input_=document.getElementById('txtTM');input_.value='"+borrow_well+"'")
        submit_button=driver.find_element_by_id("SerachButton")
        submit_button.click()


        #如果数据库里没有记录，放弃这次循环
        try:
            #对找不到的井处理
            table=driver.find_element_by_id('grdItems')
            table_list_elements=[]

        except :
            continue

        #获取表格里的所有数据条
        table_list_elements.extend(table.find_elements_by_class_name('grid_autoGenerate'))
        table_list_elements.extend(table.find_elements_by_class_name('grid_rows'))

        #档案号
        index_No=table_list_elements[0].find_elements_by_class_name('grid_item')[8].text.split('-')[2]

        #要取文件的remark,包括电子版的和非电子版本的都需要统计
        file_names=''
        _no_digital_file_names=''
        _has_digital_file_names=''
        file_numbers=0

        #查询
        for element in table_list_elements:
            #是否要这个条目的标志
            flag=True
            test_well_flag=True
            #获取井信息
            #是否有电子
            is_digital=element.find_elements_by_class_name('grid_item')[0].text
            file_name=(element.find_elements_by_class_name('grid_itemLocked')[1].text)
            #井名
            well_name=element.find_elements_by_class_name('grid_item')[1].text

            #-----------------------------规则---------------------------------------
            #没有电子版本
            _no_digital_flag=(is_digital=='无')

            #有电子版本
            _has_digital_flag=(is_digital=='[有]')        

            #对测井的条目进行排除
            for test_well in test_well_list:
                test_well_flag=test_well_flag&(file_name.find(test_well)<0)


            #如果要完井图
            if finished_picture:pass
            else:
                #判断文件名中包含完井图的字样
                finished_picture_bool=False
                for finished_picture_flag in finished_picture_flag_list:
                    finished_picture_bool=finished_picture_bool|(file_name.find(finished_picture_flag)>-1)

                #如果有一条击中，就不要这条记录
                if(finished_picture_bool):
                    flag=flag&False

            #如果要试油总结
            if oil_experiment:pass
            else:
                #判断文件名中包含试油的字样
                oil_experiment_bool=False

                for oil_experiment in oil_experiment_flag_list:
                    oil_experiment_bool=oil_experiment_bool|(file_name.find(oil_experiment)>-1)

                #如果有一条击中，就不要这条记录
                if oil_experiment_bool:
                    flag=flag&False

            #如果要完井总结
            if finished_report:pass
            else:
                #判断文件名中包含完井的字样
                finished_report_bool=False
                for finished_report_flag in  finished_report_flag_list:
                    finished_report_bool=finished_report_bool|(file_name.find(finished_report_flag)>-1)

                #如果有一条击中，就不要这条记录
                if finished_report_bool:
                    flag=flag&False        

            #如果要要岩心
            if core_analysis:pass
            else:
                #不要文件名中包含岩心总结的字样
                core_analysis_bool=False
                for core_analysis_flag in core_analysis_flag_list:
                    core_analysis_bool=core_analysis_bool|(file_name.find(core_analysis_flag)>-1)

                #如果有一条击中，就不要这条记录
                if core_analysis_bool:
                    flag=flag&False

            #---------------------------------开始汇总-------------------------------------

            #排除不要的没有电子版的    
            if (flag&_no_digital_flag&test_well_flag):

                _no_digital_file_names+=file_name+'\n'

                file_numbers=file_numbers+1

            #排除不要的有电子版的
            if ((not flag)|(_has_digital_flag&test_well_flag)):

                _has_digital_file_names+='不要'+file_name+'\n'

        #-------数目大于5的全掏
        if (file_numbers>5):

            #如果数目大于5 但是没有任何电子文件，就全掏
            if (_has_digital_file_names==''):
                file_names='全掏'
            #如果有电子文件的话列举出来
            else:
                file_names=_has_digital_file_names
                
        #小于5
        else:

            #是0的话一本不要
            if (file_numbers==0):

                file_names='一本不要'
            #不是0的话列举出来
            else:
                file_names=_no_digital_file_names  

        print('序号：',index_,file_names)

        #间歇
        time.sleep(0.01)
        borrow_table_copy.ix[index_,'井号']=borrow_table.ix[index_,'井号']
        borrow_table_copy.ix[index_,'录井图']=borrow_table.ix[index_,'录井图']
        borrow_table_copy.ix[index_,'试油总结']=borrow_table.ix[index_,'试油总结']
        borrow_table_copy.ix[index_,'完井报告']=borrow_table.ix[index_,'完井报告']
        borrow_table_copy.ix[index_,'岩心分析']=borrow_table.ix[index_,'岩心分析']
        borrow_table_copy.ix[index_,'房间号聚合']=calc_room(int(index_No),well_name)
        borrow_table_copy.ix[index_,'地址排序']=index_No
        borrow_table_copy.ix[index_,'备注(文件名)']=file_names

        if index_%5==0:
            borrow_table_copy.to_csv('./下载/缓存_满5个存一批.csv')
    
    file_name='./下载/'+str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)+first_well_name+'---'+borrow_well+'.csv'
    #最终保存
    borrow_table_copy.to_csv(file_name)
    
    
window=tk.Tk()
window.title('web_spider')
window.geometry('300x100')

var=tk.StringVar()

l=tk.Label(textvar=var,bg='yellow',width=50,height=2)
l.pack()
var.set('掏资料软件')
b=tk.Button(text='自动登录和下载',width=20,height=2,command=click_func)
b.pack()
m=tk.Message()
m.pack()
window.mainloop()
