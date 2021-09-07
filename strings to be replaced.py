def sort_eryde_keyword():
    eryde_fonts = [['UberMove-Bold.otf', 'Roboto-Bold.otf'],
                   ['UberMove-Medium.otf', 'Roboto-Medium.otf'],
                   ['UberMoveMono-Medium.otf', 'Roboto-Medium.otf'],
                   ['UberMoveMono-Regular.otf', 'Roboto-Regular.otf'],
                   ['UberMoveText-Bold.otf', 'Roboto-Bold.otf'],
                   ['UberMoveText-Light.otf', 'Roboto-Light.otf'],
                   ['UberMoveText-Medium.otf', 'Roboto-Medium.otf'],
                   ['UberMoveText-Regular.otf', 'Roboto-Regular.otf'], ]

    eryde_keywords = [['أوبر', 'eryde'], ['Uber', 'eryde'], ['UBER', 'eryde'], ['uber', 'eryde'],
                      ['ubercab', 'erydecab'], ['ub__', 'er__'], ['ub_', 'er_'],
                      ['uber_', 'eryde_'], ['ub__uber', 'er__eryde'],
                      ['ub__uberpay', 'er__erydepay'], ['ub__uberbank', 'er__erydebank'],
                      ["Uber's", "eryde's"], ['_uber', '_eryde'], ['_uber_', '_eryde_'],
                      ['_ub__', '_er__'], ['ub__ubercash', 'er__erydecash'], ]

    eryde_urls = [["https://uber.com", "https://eryde.in"],
                  ["https://uber.com/communityguidelines", "https://eryde.in/communityguidelines"],
                  ["https://www.uber.com/report-issue", "https://eryde.in/report-issue"],
                  ["https://www.uber.com/tokyo/travelagreement", "https://eryde.in/tokyo/travelagreement"],
                  ["https://www.uber.com/mainicon", "https://www.eryde.in/mainicon"],
                  ["https://www.uber.com/secondaryicon", "https://www.eryde.in/secondaryicon"],
                  ["https://www.uber.com/primaryaction", "https://www.eryde.in/primaryaction"],
                  ["http://www.uber.com/unsubscribe", "http://www.eryde.in/unsubscribe"],
                  ["https://www.uber.com/faqaudio", "https://www.eryde.in/faqaudio"],
                  ["https://www.uber.com/legal/terms", "https://www.eryde.in/legal/terms"],
                  ["https://www.uber.com/legal/privacy/users", "https://www.eryde.in/legal/privacy/users"],
                  ["https://www.uber.com/legal", "https://www.eryde.in/legal"],
                  ["https://www.uber.com/legal/safety-and-security/sos-share",
                   "https://www.eryde.in/legal/safety-and-security/sos-share"],
                  ["https://safetycenter.uber.com/trustedContacts", "https://safetycenter.eryde.in/trustedContacts"],
                  ["https://www.uber.com/us/en/coronavirus", "https://www.eryde.in/us/en/coronavirus"],
                  [
                      "https://www.uber.com/legal/en/document/?country=united-states&lang=en&name=uber-debit-card-terms-of-use",
                      "https://www.eryde.in/legal/en/document/?country=united-states&lang=en&name=eryde-debit-card-terms-of-use"],
                  [
                      "https://www.uber.com/legal/en/document/?name=user-generated-content-policy&country=united-states&lang=en",
                      "https://www.eryde.in/legal/en/document/?name=user-generated-content-policy&country=united-states&lang=en"],
                  ["https://www.uber.com/blog/order-and-pay", "https://www.eryde.in/blog/order-and-pay"],
                  ["https://www.uber.com/blog/work-hub", "https://www.eryde.in/blog/work-hub"],
                  ["https://www.uber.com/blog/new-york-city/tlc-rule-changes",
                   "https://www.eryde.in/blog/new-york-city/tlc-rule-changes"],
                  [
                      "https://help.uber.com/riders/article/envoyer-une-demande-au-responsable-de-la-protection-des-donnees-duber",
                      "https://help.eryde.in/riders/article/envoyer-une-demande-au-responsable-de-la-protection-des-donnees-deryde"],
                  ["https://help.uber.com", "https://help.eryde.in"],
                  ["https://get.uber.com/app-signup-success", "https://get.eryde.in/app-signup-success"],
                  ["https://get.uber.com/app-signup", "https://get.eryde.in/app-signup"],
                  ["https://ubr.to/sign-in-help", "https://erdye.in/sign-in-help"],
                  ["https://ubr.to/2-step-help", "https://erdye.in/2-step-help"],
                  ["https://ubr.to/location-use-info", "https://erdye.in/location-use-info"],
                  ["https://ubr.to/android-app-gifting", "https://erdye.in/android-app-gifting"],
                  ["https://privacy.uber.com", "https://privacy.eryde.in"],
                  ["https://privacy.uber.com/policy", "https://privacy.eryde.in/policy"],
                  ["https://www.nauto.com/uber-offer", "https://www.nauto.com/eryde-offer"],
                  ["https://partners.uber.com/join", "https://partners.eryde.in/join"],
                  ["https://partners.uber.com/vehicles", "https://partners.eryde.in/vehicles"],
                  ["https://partners.uber.com/p3/drivers/vehicles/index",
                   "https://partners.eryde.in/p3/drivers/vehicles/index"],
                  ["https://partners.uber.com/p3/instant_pay/faq", "https://partners.eryde.in/p3/instant_pay/faq"],
                  ["https://partners.uber.com/p3/promotions/planning",
                   "https://partners.eryde.in/p3/promotions/planning"],
                  ["https://partners.uber.com/p3/promotions/carbon-byoq",
                   "https://partners.eryde.in/p3/promotions/carbon-byoq"],
                  ["https://partners.uber.com/p3/promotions/ct-details",
                   "https://partners.eryde.in/p3/promotions/ct-details"],
                  ["https://partners.uber.com/p3/promotions/quest-details",
                   "https://partners.eryde.in/p3/promotions/quest-details"],
                  ["https://partners.uber.com/p3/promotions/carbon-calendar",
                   "https://partners.eryde.in/p3/promotions/carbon-calendar"],
                  ["https://partners.uber.com/p3/promotions/carbon-discount-byoq?native_promo_hub=true",
                   "https://partners.eryde.in/p3/promotions/carbon-discount-byoq?native_promo_hub=true"],
                  ["https://partners.uber.com/p3/promotions/quest-discount-details",
                   "https://partners.eryde.in/p3/promotions/quest-discount-details"],
                  ["https://partners.uber.com/p3/promotions/packages",
                   "https://partners.eryde.in/p3/promotions/packages"],
                  ["https://partners.uber.com/p3/payments/cartop", "https://partners.eryde.in/p3/payments/cartop"],
                  ["https://partners.uber.com/p3/payments/performance-hub/details",
                   "https://partners.eryde.in/p3/payments/performance-hub/details"],
                  ["https://partners.uber.com/p3/payments/ellis", "https://partners.eryde.in/p3/payments/ellis"],
                  ["https://partners.uber.com/p3/payments/hcv-driver-fixed-schedule",
                   "https://partners.eryde.in/p3/payments/hcv-driver-fixed-schedule"],
                  ["https://partners.uber.com/p3/payments/v2/trips", "https://partners.eryde.in/p3/payments/v2/trips"],
                  ["https://survey.uber.com/done", "https://survey.eryde.in/done"],
                  ["https://xlb.uber.com", "https://xlb.eryde.in"],
                  ["http://gobank.com/uber/noworries", "http://gobank.com/eryde/noworries"],
                  ["https://gratitude.uber.com/rewards", "https://gratitude.eryde.in/rewards"],
                  ["https://uber.formstack.com/forms/rewards_waitlist?field69750570=%s",
                   "https://eryde.formstack.com/forms/rewards_waitlist?field69750570=%s"],
                  ["https://mobile-content.uber.com/driver-platform/scheduler/youre_the_boss_badge@3x.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/youre_the_boss_badge@3x.png"],
                  ["https://mobile-content.uber.com/driver-platform/scheduler/early_access_badge@3x.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/early_access_badge@3x.png"],
                  ["https://mobile-content.uber.com/driver-platform/scheduler/go_online_with_certainty_badge@3x.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/go_online_with_certainty_badge@3x.png"],
                  ["https://mobile-content.uber.com/emobility/referral/referrral_banner%402x.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/referrral_banner%402x.png"],
                  ["https://mobile-content.uber.com/emobility/mobile-presentation/cityscoot_moto_display_image.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/cityscoot_moto_display_image.png"],
                  ["https://mobile-content.uber.com/emobility/referral/referral_ride_banner%402x.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/referral_ride_banner%402x.png"],
                  ["https://mobile-content.uber.com/delete-account/confirmation-small.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/confirmation-small.png"],
                  ["https://mobile-content.uber.com/delete-account/confirmation.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/confirmation.png"],
                  ["https://mobile-content.uber.com/eats/r2e_careem.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/r2e_careem.png"],
                  ["https://mobile-content.uber.com/eats/r2e_zomato.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/r2e_zomato.png"],
                  ["https://mobile-content.uber.com/emobility/citizen/feedbackNegative_SadFaceGraphics.json",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/feedbackNegative_SadFaceGraphics.json"],
                  ["https://mobile-content.uber.com/emobility/citizen/feedbackPositive_HappyFaceGraphics.json",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/feedbackPositive_HappyFaceGraphics.json"],
                  ["https://mobile-content.uber.com/emobility/citizen/feedbackPositive_SmilePopGraphics.json",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/feedbackPositive_SmilePopGraphics.json"],
                  ["https://d1goeicueq33a8.cloudfront.net/Ring/Icon/interstitial_safety_shield.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/interstitial_safety_shield.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/vehicle-solutions/hourly_rentals/bikes/leap/leap_bike_icon.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/leap_bike_icon.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/vehicle-solutions/hourly_rentals/bikes/leap/leap_bike_with_coin_icon.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/leap_bike_with_coin_icon.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/vehicle-solutions/hourly_rentals/bikes/leap/leap_scooter_icon.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/leap_scooter_icon.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/vehicle-solutions/hourly_rentals/bikes/leap/leap_lime_scooter_icon.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/leap_lime_scooter_icon.png"],
                  ["https://s3.amazonaws.com/uber-static/firefly/beacon_settings_bg.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/beacon_settings_bg.png"],
                  [
                      "https://s3.amazonaws.com/uber-static/vehicle-solutions/hourly_rentals/carbon/VehicleHubEmpty%402x.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/VehicleHubEmpty%402x.png"],
                  [
                      "https://d3ktknrqa34sgg.cloudfront.net/uploads/images/Dfj9I5oJjgfs+3i0oc+zjmzJfXPxATG0D0yLErFFgeg=/2019-05-06/ub__ic_uber_break_go_offline_bottom_sheet-7df5a1c0-7038-11e9-876b-bd8f31d6de35.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/er__ic_eryde_break_go_offline_bottom_sheet-7df5a1c0-7038-11e9-876b-bd8f31d6de35.png"],
                  [
                      "https://d3ktknrqa34sgg.cloudfront.net/uploads/images/P+vUslJAvP6m3loxn17VCemEJdfOJDNSqJ2buVRjltI=/2019-10-28/uber_break_uber_eats_pro_banner-2d3eff00-f9b9-11e9-a2e8-01b824e07182.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/eryde_break_eryde_eats_pro_banner-2d3eff00-f9b9-11e9-a2e8-01b824e07182.png"],
                  [
                      "https://d3ktknrqa34sgg.cloudfront.net/uploads/images/P+vUslJAvP6m3loxn17VCemEJdfOJDNSqJ2buVRjltI=/2019-10-28/uber_break_uber_pro_banner-a5d68640-f9b4-11e9-a2e8-01b824e07182.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/eryde_break_eryde_pro_banner-a5d68640-f9b4-11e9-a2e8-01b824e07182.png"],
                  ["https://d1w2poirtb3as9.cloudfront.net/a662353b1fdcf2bd5d18.jpeg",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/a662353b1fdcf2bd5d18.jpeg"],
                  ["https://rewards.uber.com/partners/hub/program-details/?in_app=true",
                   "https://rewards.eryde.in/partners/hub/program-details/?in_app=true"],
                  ["https://m2.uber.com", "https://m2.eryde.in"],
                  ["http://m.uber.com/ul", "http://m.eryde.in/ul"],
                  ["https://m.uber.com/ul", "https://m.eryde.in/ul"],
                  ["https://m.uber.com/ul/feedpermalink/?uuid=", "https://m.eryde.in/ul/feedpermalink/?uuid="],
                  ["https://login.uber.com", "https://login.eryde.in"],
                  ["https://auth.uber.com/login/forgot-password", "https://auth.eryde.in/login/forgot-password"],
                  ["https://myprivacy.uber.com/privacy/deleteyouraccount",
                   "https://myprivacy.eryde.in/privacy/deleteyouraccount"],
                  ["https://riders.uber.com", "https://riders.eryde.in"],
                  ["https://auth.uber.com/login/logout?next_url=https://uber.com",
                   "https://auth.eryde.in/login/logout?next_url=https://eryde.in"],
                  ["https://play.google.com/store/apps/details?id=com.ubercab.driver",
                   "https://play.google.in/store/apps/details?id=com.erydecab.driver"],
                  ["https://cars.cartrawler.com/uber", "https://cars.cartrawler.in/eryde"],
                  ["http://t.uber.com/uber-card-faq-v2", "http://t.eryde.in/eryde-card-faq-v2"],
                  ["http://t.uber.com/uber-card-faq", "http://t.eryde.in/eryde-card-faq"],
                  ["http://t.uber.com/metro-android", "http://t.eryde.in/metro-android"],
                  ["http://t.uber.com/driver-destination", "http://t.eryde.in/driver-destination"],
                  ["http://t.uber.com/benefitsACH", "http://t.eryde.in/benefitsACH"],
                  ["https://partners.uber.com/p3/rewards/rider/ratings",
                   "https://partners.eryde.in/p3/rewards/rider/ratings"],
                  ["https://www.uber.com/legal/business/dashboard/en-US",
                   "https://www.eryde.in/legal/business/dashboard/en-US"],
                  ["https://business.uber.com", "https://business.eryde.in"],
                  ["https://www.ubereats.com/search", ""],
                  ["http://www.ubereats.com", ""],
                  ["https://www.uber.com/legal/business/ubereats/en-US",
                   "https://www.eryde.in/legal/business"],
                  ["https://d1a3f4spazzrp4.cloudfront.net/partnerships-program/cobrand/Card_Added_Successfully.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/Card_Added_Successfully.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/partnerships-program/cobrand/Uber_Biolumin_Cards_v1_Angle_2B.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/eryde_Biolumin_Cards_v1_Angle_2B.png"],
                  ["https://d1a3f4spazzrp4.cloudfront.net/partnerships-program/cobrand/card_without_name%402x.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/card_without_name@2x.png.png"],
                  ["https://d1a3f4spazzrp4.cloudfront.net/partnerships-program/cobrand/Redemption_Angled_Card.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/Redemption_Angled_Card.png"],
                  ["https://d1a3f4spazzrp4.cloudfront.net/partnerships-program/cobrand/Payment_page_asset%403x.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/Payment_page_asset@3x.png.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/vehicle-solutions/hourly_rentals/bikes/leap/misc/Scan_QR@2x.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/Scan_QR@2x.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/vehicle-solutions/hourly_rentals/bikes/information_fare_ic.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/information_fare_ic.png"],
                  ["https://mobile-content.uber.com/emobility/mobile-presentation/trip_map_default.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/trip_map_default.png"],
                  ["https://mobile-content.uber.com/emobility/mobile-presentation/receipt_route_history_default_v2.jpg",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/receipt_route_history_default_v2.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/vehicle-solutions/hourly_rentals/bikes/information_battery_ic.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/information_battery_ic.png"],
                  [
                      "https://d1a3f4spazzrp4.cloudfront.net/vehicle-solutions/hourly_rentals/bikes/image_rider_rebalancing_intro_v2.png",
                      "https://eryde-web-media.s3.ap-south-1.amazonaws.com/image_rider_rebalancing_intro_v2.png"],
                  ["https://mobile-content.uber.com/emobility/bikes/information_zone_ic.png",
                   "https://eryde-web-media.s3.ap-south-1.amazonaws.com/information_zone_ic.png"],
                  ]

    eryde_apis = [["https://bonjour.uber.com/vehicles/add", ""],
                  ["https://bonjour.uber.com/marketplace", ""],
                  ["https://ubr.to/android-email-otp-help", ""],
                  ["https://accounts.uber.com/m/two-step", ""],
                  ["https://driverinjuryprotection.uber.com", ""],
                  ["https://driverinjuryprotection.uber.com/exit", ""],
                  ["https://cn-geo1.uber.com", ""],
                  ["https://cn-phx2.uber.com", ""],
                  ["https://cn-dc1.uber.com/ramen/events/recv", ""],
                  ["https://wisdom.uberinternal.com/report", ""],
                  ["https://code.uberinternal.com/w/teams/growth/xp/treatmentgroupmismatch", ""],
                  ["https://code.uberinternal.com", ""],
                  ["https://platform.uberinternal.com/components/buttons", ""],
                  ["https://platform.uberinternal.com/components/text-fields", ""],
                  ["https://platform.uberinternal.com/components/controls", ""],
                  ["https://platform.uberinternal.com/resources/icons", ""],
                  ["https://platform.uberinternal.com/components/lists", ""],
                  ["https://platform.uberinternal.com/components/alerts", ""],
                  ["https://platform.uberinternal.com/components/tabs", ""],
                  ["https://platform.uberinternal.com/carbon/components/buttons", ""],
                  ["https://platform.uberinternal.com/carbon/visual-system/color", ""],
                  ["https://platform.uberinternal.com/carbon/components/controls", ""],
                  ["https://platform.uberinternal.com/carbon/visual-system/icons-2", ""],
                  ["https://platform.uberinternal.com/carbon/components/lists", ""],
                  ["https://platform.uberinternal.com/carbon/components/tabs", ""],
                  ["https://platform.uberinternal.com/carbon/visual-system/typography", ""],
                  ["https://auth.uber.com/login/mobile-captcha.html", ""],
                  ["https://%s.uber.com/%s", ""],
                  ["https://gratitude.uber.com/rewards", ""],
                  ["http://hmns.kr/?M-lonlat=%s:%s&from=com.ubercab.driver&auth=UCA9_R131_P731_17", ""], ]
    for j in range(len(eryde_fonts)):
        for j_ in range(0, len(eryde_fonts) - j - 1):
            if len(eryde_fonts[j_][0]) < len(eryde_fonts[j_ + 1][0]):
                eryde_fonts[j_], eryde_fonts[j_ + 1] = eryde_fonts[j_ + 1], eryde_fonts[j_]

    for j in range(len(eryde_keywords)):
        for j_ in range(0, len(eryde_keywords) - j - 1):
            if len(eryde_keywords[j_][0]) < len(eryde_keywords[j_ + 1][0]):
                eryde_keywords[j_], eryde_keywords[j_ + 1] = eryde_keywords[j_ + 1], eryde_keywords[j_]

    for j in range(len(eryde_urls)):
        for j_ in range(0, len(eryde_urls) - j - 1):
            if len(eryde_urls[j_][0]) < len(eryde_urls[j_ + 1][0]):
                eryde_urls[j_], eryde_urls[j_ + 1] = eryde_urls[j_ + 1], eryde_urls[j_]

    for j in range(len(eryde_apis)):
        for j_ in range(0, len(eryde_apis) - j - 1):
            if len(eryde_apis[j_][0]) < len(eryde_apis[j_ + 1][0]):
                eryde_apis[j_], eryde_apis[j_ + 1] = eryde_apis[j_ + 1], eryde_apis[j_]

    return eryde_fonts, eryde_keywords, eryde_urls, eryde_apis


eryde_fonts, eryde_keywords, eryde_urls, eryde_apis = sort_eryde_keyword()

import os

from tqdm import tqdm

project_path = r"C:\Users\user\Desktop\app\eryde driver\eryde_driver"

for root, dirs, files in tqdm(os.walk(project_path, topdown=False)):
    for name in files:
        temp_filepath = os.path.join(root, name)
        temp_old_filepath = temp_filepath
        e_api_found, writable_lines = [], []

        try:
            file = str(open(temp_filepath, "rb").read())
            for line in file:
                # eryde_apis
                for e_api in eryde_apis:
                    if e_api[0] in line:
                        e_api_found.append(e_api)
                # eryde_fonts
                for e_font in eryde_fonts:
                    if e_font[0] in line:
                        line = line.replace(bytes(e_font[0]), e_font[1])
                # eryde_urls
                for e_url in eryde_urls:
                    if e_url[0] in line:
                        line = line.replace(bytes(e_url[0]), e_url[1])
                # eryde_keywords
                for e_keyword in eryde_keywords:
                    if e_keyword[0] in temp_filepath:
                        temp_filepath = temp_filepath.replace(e_keyword[0], e_keyword[1])

                    if e_keyword[0] in line:
                        if e_api_found:
                            for e_api in e_api_found:
                                if e_keyword[0] in e_api:
                                    continue
                                else:
                                    line = line.replace(bytes(e_keyword[0]), e_keyword[1])
                        else:
                            line = line.replace(bytes(e_keyword[0]), e_keyword[1])
                writable_lines.append(line)
            file.close()

            # check that new directory exists or not
            temp_dir = temp_filepath.rsplit("\\", 1)[0]
            if not os.path.exists(temp_dir):
                if os.path.exists(temp_old_filepath):
                    os.remove(temp_old_filepath)
                os.makedirs(temp_dir)
            file = open(temp_filepath, 'w')
            file.writelines(writable_lines)
            file.close()

        except UnicodeDecodeError as e:
            pass
        except Exception as  e:
            pass
