import unittest
import otp
import sender_data

class TestingOTPSender(unittest.TestCase):
    def assertBetween(self, x, low, hi):
        if not (low <= x <= hi):
            raise AssertionError(
                'Length of OTP should be in between %r and %r' %(low, hi)

            )

    def test_generateOTP(self):
        size = 5
        Otp = otp.generateOTP(size)

        self.assertEqual(len(Otp), size, 'OTP length does not match')
        self.assertBetween(len(Otp), 4, 8)

    def test_verifyOTP(self):
        Otp = otp.generateOTP(4)

        self.assertTrue(otp.verifyOTP(Otp, Otp), "OTP does not match")
        self.assertFalse(otp.verifyOTP(Otp, 'abcd'),
                            "OTP should not have matched")

    def test_validateEmail(self):
        receiver_email = 'username@domain.in'

        self.assertIn('@', receiver_email, "Email is not valid")
        self.assertIn('.in', receiver_email, "Email is not valid")

    def test_validateEmail2(self):
        receiver_email = 'username@domain.com'

        self.assertIn('@', receiver_email, "Email is not valid")
        self.assertIn('.com', receiver_email, "Email is not valid")

    def test_sendOTP(self):
        Otp = otp.generateOTP(5)
        receiver_email = 'poojasawant@dbatu.ac.in'


        self.assertBetween(len(Otp), 4, 8)
        self.assertIn('@', receiver_email, "Email is not valid")
        self.assertIn('.in', receiver_email, "Email is not valid")

        otp.sendOTP(sender_data,receiver_email, Otp)

if __name__ == '__main__':
    unittest.main()