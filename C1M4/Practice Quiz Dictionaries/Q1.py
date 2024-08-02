def email_list(domains):
	emails = []
	for key, values in domains.items():
		for value in values:
			emails.append(value + '@' + key)
	return(emails)

print(email_list(
	{
		"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
		"yahoo.com": ["barbara.gordon", "jean.grey"],
		"hotmail.com": ["bruce.wayne"]
	}))