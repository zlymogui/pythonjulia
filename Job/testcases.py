#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 单个用例执行
# 1、导入模块
import unittest
from Fetch_Transaction_API import FetchTransactionAPI


# 2、继承自unittest.TestCase类
class MyTestSuite(unittest.TestCase):
    # 3、配置环境：进行测试前的初始化工作，比如在接口测试前面做一些前置的参数赋值， 数据库操作等等。
    def setUp(self):
        print('\ncases before')
        pass

    # 4、定义测试用例，名字以“test”开头，testcase的执行顺序是按字母排序
    def test_add(self):
        '''test add method'''
        print('add...')
        a = 5 + 2
        b = 7
        # 5、定义assert断言，判断测试结果
        self.assertEqual(a, b)

    def test_sub(self):
        '''test sub method'''
        print('sub...')
        a = 10 - 5
        b = 6
        self.assertEqual(a, b)

    def test_register_api(self): # 2.用户注册(CustomerAdd)
        pass

    def test_fetch_customer_id_api(self): # 3.用手机查找用户ID(Retrieve CustomerID by mobile)
        pass

    def test_fetch_customer_details_api(self): # 4.获取用户信息(Retrieve customer information)
        pass

    def test_update_customer_details_api(self): #5.更新用户信息(CustomerUpdate)
        pass

    def test_update_customer_identifiers_api(self): #6.	更新用户Identifier
        pass

    def test_check_if_points_are_redeemable_api(self): #7.检查积分是否可用(Check points are redeemable)
        pass

    def test_redeem_points_api(self): #8.扣减积分(Redeem points)
        pass

    def test_add_promotion_points_api(self): #8.发放活动积分(issue points)
        pass

    def test_issue_coupon_api(self): #9.发放优惠券(Issue coupon)
        pass

    def test_redeem_coupon_api(self):#10.核销优惠券(Redeem coupon)
        pass

    def test_retrieve_coupon_series_details_api(self):#11.查询客户优惠券列表(Retrieve customer coupons)
        pass

    def test_add_transaction_api(self): #购买
        pass

    def test_add_transaction_api(self): #退货
        pass

    def test_add_transaction_api(self): #换货
        pass

    def test_get_user_tracker_api(self): #13.获取用户经验值(GetUserTracker)
        pass

    def test_get_transaction_points_history_api(self): #14.1获取积分历史1)获取交易积分历史
        pass

    def test_get_activity_points_history_api(self): #14.1获取积分历史2)获取活动积分历史
        pass

    def test_get_points_redeem_history_api(self): #14.2 消费积分获取历史（PointsRedeemHistory）
        pass

    def test_get_points_expired_history_api(self): #14.3 获取过期积分总数（ExpiredPointsTotal)
        pass


    def test_fetch_transaction_api(self):
        resp_code,resp_message = FetchTransactionAPI.FetchTransaction.FetchTransactionDetails("JULIA5173680481")
        print(resp_code)
        self.assertEqual(resp_code,600, "successfully")

    # 6、清理环境。测试后的清除工作，比如参数还原或销毁，数据库的还原恢复等
    def tearDown(self):
        print('case after')
        pass

if __name__ == "__main__":
    #apitest = MyTestSuite()
    unittest.main() # 调用unittest.main()启动测试