num_steps = 3
path = '../ex01/data.csv'
output_file_name = 'report'
extension_file = 'txt'
template_text = "We have made {} observations from tossing a coin: {} of them were tails and {} of them were heads. The probabilities are {:.2f}% and {:.2f}%, respectively. Our forecast is that in the next {} observations we will have: {} tail and {} heads."
log_file='analitics.log'
logging_format = "%(asctime)s : %(message)s"
create_report = 'The report has been successfully created'
not_creat_report = 'The report hasn’t been created due to an error'
url_to_send = 'https://hooks.slack.com/services/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'