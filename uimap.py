# Web elements locators

HomePageMap = dict(SignInButtonXpath = "//a[contains(@title, 'Log in to your customer account')]",
                   SearchQueryTextField = "search_query_top",
                   WomenTabXpath = "//a[@title='Women']")

LoginPageMap = dict(FirstNameID = "customer_firstname",
                    LastNameID = "customer_lastname",
                    PasswordID = "passwd",
                    CompanyID = "company",
                    Address1ID = "address1",
                    CityID = "city",
                    PostalID = "postcode",
                    PhoneID = "phone_mobile",
                    AliasID = "alias",
                    StateID = "id_state",
                    CountryID = "id_country",
                    RegisterButtonID = "submitAccount")

OrderPageMap = dict(EmailID = "email",
                    PasswordID = "passwd",
                    SubmitLoginButtonID = "SubmitLogin",
                    CheckboxID = "cgv",
                    ProceedToCheckOutAddressTabButtonName = "processAddress",
                    ProceedToCheckOutOrderTabButtonName = "processCarrier",
                    PayByCheckButtonXpath = "//a[contains(@title, 'Pay by check')]",
                    ConfirmOrderButton = "submit_search")

SpecificDressPageMap = dict(QuantityID = "quantity_wanted",
                            AddToCartButtonID = "add_to_cart",
                            ProceedToCheckOutButtonXpath = "//a[contains(@title, 'Proceed to checkout')]")

WomenPageMap = dict(DressesSubcategoryXpath = "//img[contains(@src,'http://automationpractice.com/img/c/8-medium_default.jpg')]")

EveningPageMap = dict(PrintedDressXpath = "//img[contains(@src, 'http://automationpractice.com/img/p/1/0/10-home_default.jpg')]")

DressesPageMap = dict(EveningDressesSubcategoryXpath = "//img[contains(@src,'http://automationpractice.com/img/c/10-medium_default.jpg')]")

