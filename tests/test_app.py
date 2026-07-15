import unittest

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_predict_shows_approved_result(self):
        response = self.client.post(
            "/predict",
            data={
                "Gender": "Male",
                "Married": "Yes",
                "ApplicantIncome": "5000",
                "LoanAmount": "150",
                "Credit_History": "1",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("Loan Approved", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
