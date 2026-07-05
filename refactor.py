import re

with open('c:/xampp/htdocs/ananya/index.php', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. section-desc-lg
content = content.replace('style=\"font-size: 18px; color: #777; line-height: 1.8;\"', 'class=\"section-desc-lg\"')
content = content.replace('class=\"mb-4\" class=\"section-desc-lg\"', 'class=\"mb-4 section-desc-lg\"')

# 2. text-secondary-light
content = content.replace('style=\"color: #999 !important;\"', 'class=\"text-secondary-light\"')
content = content.replace('class=\"italic-serif text-secondary\" class=\"text-secondary-light\"', 'class=\"italic-serif text-secondary text-secondary-light\"')

# 3. hero-card-banner
content = content.replace('style=\"height: 500px; border-radius: 20px;\"', 'class=\"hero-card-banner\"')
content = content.replace('class=\"image-card w-100\" class=\"hero-card-banner\"', 'class=\"image-card w-100 hero-card-banner\"')

# 4. overlay-subtitle & overlay-title-lg
content = content.replace('style=\"font-size: 14px; letter-spacing: 1px; margin-top: 0; color: #ccc;\"', 'class=\"overlay-subtitle\"')
content = content.replace('class=\"text-uppercase mb-2\" class=\"overlay-subtitle\"', 'class=\"text-uppercase mb-2 overlay-subtitle\"')
content = content.replace('style=\"font-size: 48px; margin: 0;\"', 'class=\"overlay-title-lg\"')

# 5. feature-title & feature-desc
content = content.replace('style=\"font-size: 20px; font-weight: 500; color: #333;\"', 'class=\"feature-title\"')
content = content.replace('class=\"mb-3\" class=\"feature-title\"', 'class=\"mb-3 feature-title\"')
content = content.replace('style=\"font-size: 15px; color: #777; line-height: 1.6;\"', 'class=\"feature-desc\"')

# 6. text-primary-blue
content = content.replace('style=\"color: #0b4b8a;\"', 'class=\"text-primary-blue\"')
content = content.replace('class=\"italic-serif\" class=\"text-primary-blue\"', 'class=\"italic-serif text-primary-blue\"')

# 7. rounded-banner-img
content = content.replace('style=\"border-radius: 24px; object-fit: cover; height: 550px;\"', 'class=\"rounded-banner-img\"')
content = content.replace('class=\"w-100\" class=\"rounded-banner-img\"', 'class=\"w-100 rounded-banner-img\"')

# 8. border-bottom-light
content = content.replace('style=\"border-bottom: 1px solid #eaeaea;\"', 'class=\"border-bottom-light\"')
content = content.replace('class=\"why-feature-box pb-5\" class=\"border-bottom-light\"', 'class=\"why-feature-box pb-5 border-bottom-light\"')

# 9. feature-desc-sm
content = content.replace('style=\"font-size: 15px; color: #777; line-height: 1.6; margin: 0;\"', 'class=\"feature-desc-sm\"')

# 10. process-wrapper
content = content.replace('style=\"background-color: #fafbfc; padding: 100px;\"', 'class=\"process-wrapper-bg\"')
content = content.replace('class=\"process-wrapper position-relative rounded-4\" class=\"process-wrapper-bg\"', 'class=\"process-wrapper position-relative rounded-4 process-wrapper-bg\"')

# 11. decorative dots
content = content.replace('style=\"top: 80px; left: -20px; z-index: 2;\"', 'class=\"dots-top-left\"')
content = content.replace('class=\"position-absolute d-none d-lg-flex align-items-center\" class=\"dots-top-left\"', 'class=\"position-absolute d-none d-lg-flex align-items-center dots-top-left\"')
content = content.replace('style=\"width: 150px; height: 2px; background-color: #f26522;\"', 'class=\"dot-line\"')
content = content.replace('style=\"width: 16px; height: 16px; background-color: #f26522; border-radius: 50%; margin: 0 4px;\"', 'class=\"dot-circle\"')
content = content.replace('style=\"width: 16px; height: 16px; background-color: #f26522; opacity: 0.6; border-radius: 50%; margin: 0 4px;\"', 'class=\"dot-circle-md\"')
content = content.replace('style=\"width: 16px; height: 16px; background-color: #f26522; opacity: 0.3; border-radius: 50%; margin: 0 4px;\"', 'class=\"dot-circle-sm\"')
content = content.replace('style=\"bottom: 40px; right: -20px; z-index: 2;\"', 'class=\"dots-bottom-right\"')
content = content.replace('class=\"position-absolute d-none d-lg-flex align-items-center\" class=\"dots-bottom-right\"', 'class=\"position-absolute d-none d-lg-flex align-items-center dots-bottom-right\"')

# 12. border-light-custom
content = content.replace('style=\"border-color: #ebebeb !important;\"', 'class=\"border-light-custom\"')
content = content.replace('class=\"col-4 border-end pe-4\" class=\"border-light-custom\"', 'class=\"col-4 border-end pe-4 border-light-custom\"')
content = content.replace('class=\"col-4 border-end px-4\" class=\"border-light-custom\"', 'class=\"col-4 border-end px-4 border-light-custom\"')

# 13. icon-box-shadow
content = content.replace('style=\"box-shadow: 0 10px 20px rgba(0,0,0,0.03); width: 50px; height: 50px; color: #f26522; border-radius: 10px;\"', 'class=\"icon-box-shadow\"')
content = content.replace('class=\"icon-box-small bg-white mb-4\" class=\"icon-box-shadow\"', 'class=\"icon-box-small bg-white mb-4 icon-box-shadow\"')

# 14. process title/desc
content = content.replace('style=\"font-size: 18px; font-weight: 500; color: #333; margin-bottom: 12px;\"', 'class=\"process-title\"')
content = content.replace('style=\"font-size: 14px; color: #777; line-height: 1.6; margin: 0;\"', 'class=\"process-desc\"')

# 15. process-img-offset
content = content.replace('style=\"width: 125%; height: 400px; object-fit: cover; border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-right: -25%; display: block; position: relative; z-index: 1;\"', 'class=\"process-img-offset\"')

# 16. admissions text
content = content.replace('style=\"font-size: 54px; font-weight: 400; margin-bottom: 0;\"', 'class=\"admissions-title-top\"')
content = content.replace('style=\"font-size: 54px; font-weight: 400; margin-bottom: 30px;\"', 'class=\"admissions-title-bottom\"')
content = content.replace('class=\"italic-serif\" class=\"admissions-title-bottom\"', 'class=\"italic-serif admissions-title-bottom\"')
content = content.replace('style=\"color: #d0d0d0; font-size: 16px; line-height: 1.6; max-width: 90%;\"', 'class=\"admissions-desc\"')
content = content.replace('class=\"mb-5\" class=\"admissions-desc\"', 'class=\"mb-5 admissions-desc\"')

# 17. form styling
content = content.replace('style=\"border-radius: 20px !important;\"', 'class=\"form-card-rounded\"')
content = content.replace('class=\"form-card bg-white p-5 rounded-4\" class=\"form-card-rounded\"', 'class=\"form-card bg-white p-5 rounded-4 form-card-rounded\"')
content = content.replace('style=\"font-size: 26px; color: #333; font-weight: 500;\"', 'class=\"form-heading\"')
content = content.replace('class=\"mb-2\" class=\"form-heading\"', 'class=\"mb-2 form-heading\"')
content = content.replace('style=\"font-size: 15px; color: #888;\"', 'class=\"form-subheading\"')
content = content.replace('class=\"mb-5\" class=\"form-subheading\"', 'class=\"mb-5 form-subheading\"')
content = content.replace('style=\"font-size: 13px; font-weight: 600; color: #333;\"', 'class=\"form-label-custom\"')
content = content.replace('class=\"form-label\" class=\"form-label-custom\"', 'class=\"form-label form-label-custom\"')

# 18. form button
content = content.replace('style=\"padding: 15px 30px; border-radius: 40px; display: flex; justify-content: space-between; align-items: center; max-width: 250px;\"', 'class=\"btn-submit-inquiry\"')
content = content.replace('class=\"btn-primary border-0 w-100 mt-2\" class=\"btn-submit-inquiry\"', 'class=\"btn-primary border-0 w-100 mt-2 btn-submit-inquiry\"')
content = content.replace('style=\"background: white; color: #0b4b8a; padding: 5px; border-radius: 50%; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; font-size: 12px;\"', 'class=\"btn-icon-circle\"')
content = content.replace('class=\"fa-solid fa-arrow-right-long\" class=\"btn-icon-circle\"', 'class=\"fa-solid fa-arrow-right-long btn-icon-circle\"')

with open('c:/xampp/htdocs/ananya/index.php', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced inline styles successfully!")
