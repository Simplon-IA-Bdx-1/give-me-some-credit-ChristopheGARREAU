import kaggle


submission_file = "prediction_kaggle.csv"

kaggle.api.competition_submit(submission_file, "BigML ensemble", "GiveMeSomeCredit")