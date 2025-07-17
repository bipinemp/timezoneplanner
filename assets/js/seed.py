import os

# Expanded timezone list with display names (60+ entries)
timezones = [
    ("Pacific/Honolulu", "Honolulu (HST)"),
    ("America/Anchorage", "Anchorage (AKST/AKDT)"),
    ("America/Los_Angeles", "Los Angeles (PST/PDT)"),
    ("America/Denver", "Denver (MST/MDT)"),
    ("America/Phoenix", "Phoenix (MST - no DST)"),
    ("America/Chicago", "Chicago (CST/CDT)"),
    ("America/New_York", "New York (EST/EDT)"),
    ("America/Toronto", "Toronto (EST/EDT)"),
    ("America/Vancouver", "Vancouver (PST/PDT)"),
    ("America/Montreal", "Montreal (EST/EDT)"),
    ("America/Halifax", "Halifax (AST/ADT)"),
    ("America/Bogota", "Bogotá (COT)"),
    ("America/Lima", "Lima (PET)"),
    ("America/Sao_Paulo", "São Paulo (BRT)"),
    ("America/Buenos_Aires", "Buenos Aires (ART)"),
    ("America/Mexico_City", "Mexico City (CST/CDT)"),
    ("America/Caracas", "Caracas (VET)"),
    ("America/Santiago", "Santiago (CLT/CLST)"),
    ("Europe/London", "London (GMT/BST)"),
    ("Europe/Dublin", "Dublin (GMT/IST)"),
    ("Europe/Madrid", "Madrid (CET/CEST)"),
    ("Europe/Berlin", "Berlin (CET/CEST)"),
    ("Europe/Paris", "Paris (CET/CEST)"),
    ("Europe/Rome", "Rome (CET/CEST)"),
    ("Europe/Amsterdam", "Amsterdam (CET/CEST)"),
    ("Europe/Brussels", "Brussels (CET/CEST)"),
    ("Europe/Vienna", "Vienna (CET/CEST)"),
    ("Europe/Warsaw", "Warsaw (CET/CEST)"),
    ("Europe/Prague", "Prague (CET/CEST)"),
    ("Europe/Budapest", "Budapest (CET/CEST)"),
    ("Europe/Zurich", "Zurich (CET/CEST)"),
    ("Europe/Stockholm", "Stockholm (CET/CEST)"),
    ("Europe/Copenhagen", "Copenhagen (CET/CEST)"),
    ("Europe/Oslo", "Oslo (CET/CEST)"),
    ("Europe/Helsinki", "Helsinki (EET/EEST)"),
    ("Europe/Athens", "Athens (EET/EEST)"),
    ("Europe/Istanbul", "Istanbul (TRT)"),
    ("Europe/Moscow", "Moscow (MSK)"),
    ("Europe/Kiev", "Kiev (EET/EEST)"),
    ("Africa/Johannesburg", "Johannesburg (SAST)"),
    ("Africa/Cairo", "Cairo (EET)"),
    ("Africa/Nairobi", "Nairobi (EAT)"),
    ("Africa/Lagos", "Lagos (WAT)"),
    ("Africa/Casablanca", "Casablanca (WET/WEST)"),
    ("Asia/Dubai", "Dubai (GST)"),
    ("Asia/Tehran", "Tehran (IRST/IRDT)"),
    ("Asia/Karachi", "Karachi (PKT)"),
    ("Asia/Kolkata", "Mumbai/Delhi (IST)"),
    ("Asia/Colombo", "Colombo (SLST)"),
    ("Asia/Dhaka", "Dhaka (BST)"),
    ("Asia/Kathmandu", "Kathmandu (NPT)"),
    ("Asia/Yangon", "Yangon (MMT)"),
    ("Asia/Bangkok", "Bangkok (ICT)"),
    ("Asia/Ho_Chi_Minh", "Ho Chi Minh City (ICT)"),
    ("Asia/Jakarta", "Jakarta (WIB)"),
    ("Asia/Singapore", "Singapore (SGT)"),
    ("Asia/Kuala_Lumpur", "Kuala Lumpur (MYT)"),
    ("Asia/Manila", "Manila (PHT)"),
    ("Asia/Hong_Kong", "Hong Kong (HKT)"),
    ("Asia/Shanghai", "Shanghai (CST)"),
    ("Asia/Taipei", "Taipei (CST)"),
    ("Asia/Seoul", "Seoul (KST)"),
    ("Asia/Tokyo", "Tokyo (JST)"),
    ("Asia/Tashkent", "Tashkent (UZT)"),
    ("Asia/Almaty", "Almaty (ALMT)"),
    ("Australia/Perth", "Perth (AWST)"),
    ("Australia/Adelaide", "Adelaide (ACST/ACDT)"),
    ("Australia/Darwin", "Darwin (ACST)"),
    ("Australia/Brisbane", "Brisbane (AEST)"),
    ("Australia/Sydney", "Sydney (AEST/AEDT)"),
    ("Australia/Melbourne", "Melbourne (AEST/AEDT)"),
    ("Pacific/Auckland", "Auckland (NZST/NZDT)"),
    ("Pacific/Fiji", "Fiji (FJT)")
]

# Expanded popular pairs (60+ combinations)
popular_pairs = [
    ("America/New_York", "Europe/London"),
    ("America/New_York", "Asia/Kolkata"),
    ("Europe/London", "Asia/Tokyo"),
    ("America/Los_Angeles", "Asia/Tokyo"),
    ("Asia/Kathmandu", "America/New_York"),
    ("Asia/Kolkata", "Europe/London"),
    ("Asia/Tokyo", "America/New_York"),
    ("Australia/Sydney", "America/New_York"),
    ("Europe/Berlin", "America/Toronto"),
    ("Asia/Singapore", "America/Chicago"),
    ("Asia/Manila", "Europe/London"),
    ("America/Chicago", "Europe/Berlin"),
    ("America/Denver", "Asia/Singapore"),
    ("Asia/Kathmandu", "Australia/Sydney"),
    ("Europe/Madrid", "America/New_York"),
    ("Europe/Paris", "America/New_York"),
    ("Europe/Amsterdam", "America/New_York"),
    ("Europe/Rome", "Asia/Tokyo"),
    ("Europe/Zurich", "Asia/Kathmandu"),
    ("Europe/Stockholm", "America/New_York"),
    ("Europe/Helsinki", "America/Chicago"),
    ("Asia/Seoul", "Europe/London"),
    ("Asia/Bangkok", "America/Toronto"),
    ("Asia/Jakarta", "America/New_York"),
    ("Asia/Dubai", "Australia/Sydney"),
    ("Asia/Hong_Kong", "America/New_York"),
    ("Asia/Taipei", "America/Chicago"),
    ("Pacific/Auckland", "Europe/London"),
    ("Pacific/Honolulu", "Asia/Tokyo"),
    ("Africa/Johannesburg", "America/New_York"),
    ("Africa/Nairobi", "Europe/London"),
    ("Asia/Colombo", "Australia/Sydney"),
    ("Asia/Karachi", "America/New_York"),
    ("America/Toronto", "Europe/London"),
    ("America/Mexico_City", "Europe/Madrid"),
    ("America/Los_Angeles", "Europe/London"),
    ("Europe/Dublin", "Asia/Tokyo"),
    ("Europe/Istanbul", "America/New_York"),
    ("Asia/Dhaka", "America/Chicago"),
    ("Asia/Yangon", "Europe/Paris"),
    ("America/Buenos_Aires", "Europe/Madrid"),
    ("America/Sao_Paulo", "Europe/Zurich"),
    ("America/Lima", "Europe/Amsterdam"),
    ("America/Bogota", "Europe/Amsterdam"),
    ("Asia/Kuala_Lumpur", "Australia/Perth"),
    ("Asia/Ho_Chi_Minh", "America/Chicago"),
    ("Asia/Kathmandu", "Europe/Zurich"),
    ("America/Anchorage", "Asia/Kolkata"),
    ("Europe/Copenhagen", "America/New_York"),
    ("Europe/Oslo", "America/Los_Angeles"),
    ("Europe/Prague", "Asia/Tokyo"),
    ("Europe/Vienna", "America/Chicago"),
    ("Europe/Brussels", "Asia/Singapore"),
    ("Europe/Warsaw", "America/Toronto"),
    ("Europe/Budapest", "Asia/Manila"),
    ("Asia/Tehran", "Europe/London"),
    ("Asia/Tashkent", "America/New_York"),
    ("Africa/Cairo", "America/Chicago"),
    ("Africa/Lagos", "Europe/Berlin"),
    ("Africa/Casablanca", "Asia/Dubai"),
    ("Australia/Melbourne", "Europe/London"),
    ("Australia/Brisbane", "America/Los_Angeles"),
    ("Australia/Darwin", "Asia/Singapore"),
    ("America/Vancouver", "Asia/Seoul"),
    ("America/Montreal", "Europe/Paris"),
    ("America/Halifax", "Asia/Tokyo"),
    ("America/Caracas", "Europe/Madrid"),
    ("America/Santiago", "Asia/Hong_Kong"),
    ("Pacific/Fiji", "America/New_York"),
    ("Europe/Kiev", "America/Chicago"),
    ("Asia/Almaty", "Europe/Berlin")
]

html_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-7WLE5SB6NX"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
        gtag('js', new Date());

        gtag('config', 'G-7WLE5SB6NX');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meeting Planner for {name1_display} and {name2_display} | Time Zone Meeting Planner</title>
    <meta name="description"
        content="Plan perfect meeting times between {name1_display} and {name2_display}. Overlapping work hours and current times displayed.">
    <meta name="keywords"
        content="time zone converter, meeting planner, international meeting times, remote work scheduler, global team coordination">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://timezoneplanner.netlify.app/{slug}.html">

    <!-- Open Graph -->
    <meta property="og:title" content="Meeting Planner: {name1_display} & {name2_display}">
    <meta property="og:description"
        content="Plan perfect meeting times between {name1_display} and {name2_display}. Overlapping work hours and current times.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://timezoneplanner.netlify.app/{slug}.html">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Meeting Planner for {name1_display} and {name2_display}">
    <meta name="twitter:description"
        content="Plan perfect meeting times between {name1_display} and {name2_display}. Overlapping work hours and current times.">

    <script src="https://cdn.jsdelivr.net/npm/luxon@3.4.4/build/global/luxon.min.js"></script>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>

<body>
    <header class="header">
        <div class="container">
            <h1 class="logo">
                <span class="logo-icon">🌍</span>
                TimeSync Pro
            </h1>

            <nav class="quick-links" role="navigation" aria-label="Popular country combinations">
                <div class="quick-links-container">
                    <a href="nepal-usa.html" class="quick-link">Nepal-USA</a>
                    <a href="india-usa.html" class="quick-link">India-USA</a>
                    <a href="uk-usa.html" class="quick-link">UK-USA</a>
                    <a href="japan-usa.html" class="quick-link">Japan-USA</a>
                    <a href="australia-usa.html" class="quick-link">Australia-USA</a>
                    <div class="search-container">
                        <input type="search" id="countrySearch" placeholder="Search countries..."
                            aria-label="Search for country combinations">
                        <button type="button" id="searchBtn" aria-label="Search">🔍</button>
                    </div>
                </div>
            </nav>
        </div>
    </header>

    <main class="main-content">
        <div class="container">
            <section class="meeting-planner" aria-labelledby="planner-heading">
                <h3 id="planner-heading" class="sr-only">Meeting Time Planner Tool</h3>

                <div class="timezone-selector">
                    <div class="timezone-group">
                        <label for="timezone1">First Location</label>
                        <select id="timezone1" aria-describedby="timezone1-desc">
                            {timezone1_options}
                        </select>
                        <div id="timezone1-desc" class="timezone-desc">Current time will be displayed here</div>
                    </div>

                    <div class="timezone-group">
                        <label for="timezone2">Second Location</label>
                        <select id="timezone2" aria-describedby="timezone2-desc">
                            {timezone2_options}
                        </select>
                        <div id="timezone2-desc" class="timezone-desc">Current time will be displayed here</div>
                    </div>

                    <div class="timezone-group optional">
                        <label for="timezone3">Third Location (Optional)</label>
                        <select id="timezone3" aria-describedby="timezone3-desc">
                            {timezone3_options}
                        </select>
                        <div id="timezone3-desc" class="timezone-desc">Current time will be displayed here</div>
                    </div>
                </div>

                <div class="work-hours-config">
                    <h4>Work Hours Configuration</h4>
                    <div class="work-hours-inputs">
                        <div class="time-input-group timezone-group">
                            <label for="timeFormat">Time Format</label>
                            <select id="timeFormat">
                                <option value="24">24-hour</option>
                                <option value="12">12-hour (AM/PM)</option>
                            </select>
                        </div>
                        <div class="time-input-group">
                            <label for="workStart">Work Start Time</label>
                            <input type="time" id="workStart" value="09:00" aria-describedby="work-hours-desc">
                        </div>
                        <div class="time-input-group">
                            <label for="workEnd">Work End Time</label>
                            <input type="time" id="workEnd" value="17:00">
                        </div>
                    </div>
                    <div id="work-hours-desc" class="help-text">Set typical work hours to find overlapping meeting times
                    </div>
                </div>

                <button type="button" id="findMeetingTimes" class="cta-button">Find Best Meeting Times</button>
            </section>

            <section id="results" class="results-section" aria-live="polite">
                <!-- Results will be populated by JavaScript -->
            </section>

            <section class="features-section">
                <h3>Why Use Our Meeting Planner?</h3>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">⏰</div>
                        <h4>Instant Results</h4>
                        <p>Get overlapping work hours instantly without manual calculations</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🌐</div>
                        <h4>Global Coverage</h4>
                        <p>Support for all major time zones and countries worldwide</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">👥</div>
                        <h4>Team Friendly</h4>
                        <p>Perfect for remote teams and international business meetings</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">📱</div>
                        <h4>Mobile Ready</h4>
                        <p>Works seamlessly on desktop, tablet, and mobile devices</p>
                    </div>
                </div>
            </section>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Popular Combinations</h4>
                    <ul>
                        <li><a href="nepal-usa.html">Nepal - USA Meeting Times</a></li>
                        <li><a href="india-usa.html">India - USA Meeting Times</a></li>
                        <li><a href="uk-usa.html">UK - USA Meeting Times</a></li>
                        <li><a href="japan-usa.html">Japan - USA Meeting Times</a></li>
                        <li><a href="australia-usa.html">Australia - USA Meeting Times</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>More Combinations</h4>
                    <ul>
                        <li><a href="germany-usa.html">Germany - USA Meeting Times</a></li>
                        <li><a href="canada-uk.html">Canada - UK Meeting Times</a></li>
                        <li><a href="singapore-usa.html">Singapore - USA Meeting Times</a></li>
                        <li><a href="philippines-usa.html">Philippines - USA Meeting Times</a></li>
                        <li><a href="bangladesh-usa.html">Bangladesh - USA Meeting Times</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="how-it-works.html">How It Works</a></li>
                        <li><a href="time-zone-guide.html">Time Zone Guide</a></li>
                        <li><a href="meeting-tips.html">Meeting Tips</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="terms-of-service.html">Terms of Service</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                        <li><a href="sitemap.html">Sitemap</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 TimeSync Pro. All rights reserved. | Making global collaboration easier.</p>
            </div>
        </div>
    </footer>

    <script src="/assets/js/script.js"></script>
</body>

</html>
"""

def build_options(selected_val=None, include_empty=False):
    options = []
    if include_empty:
        options.append('<option value="">Select timezone...</option>')
    for tz, label in timezones:
        if tz == selected_val:
            # selected option first with selected attribute
            options.insert(0, f'<option value="{tz}" selected>{label}</option>')
        else:
            options.append(f'<option value="{tz}">{label}</option>')
    return "\n".join(options)

def slugify(tz1, tz2):
    """Enhanced slugify function with comprehensive timezone mapping"""
    # Map timezone identifiers to SEO-friendly short names
    short_names = {
        # Americas
        "America/New_York": "usa",
        "America/Los_Angeles": "usa-west",
        "America/Chicago": "usa-central",
        "America/Denver": "usa-mountain",
        "America/Phoenix": "arizona",
        "America/Toronto": "canada",
        "America/Vancouver": "canada-west",
        "America/Montreal": "canada-east",
        "America/Halifax": "canada-atlantic",
        "America/Anchorage": "alaska",
        "America/Mexico_City": "mexico",
        "America/Bogota": "colombia",
        "America/Lima": "peru",
        "America/Sao_Paulo": "brazil",
        "America/Buenos_Aires": "argentina",
        "America/Caracas": "venezuela",
        "America/Santiago": "chile",
        "Pacific/Honolulu": "hawaii",
        
        # Europe
        "Europe/London": "uk",
        "Europe/Dublin": "ireland",
        "Europe/Paris": "france",
        "Europe/Berlin": "germany",
        "Europe/Madrid": "spain",
        "Europe/Rome": "italy",
        "Europe/Amsterdam": "netherlands",
        "Europe/Brussels": "belgium",
        "Europe/Vienna": "austria",
        "Europe/Zurich": "switzerland",
        "Europe/Stockholm": "sweden",
        "Europe/Copenhagen": "denmark",
        "Europe/Oslo": "norway",
        "Europe/Helsinki": "finland",
        "Europe/Warsaw": "poland",
        "Europe/Prague": "czech",
        "Europe/Budapest": "hungary",
        "Europe/Athens": "greece",
        "Europe/Istanbul": "turkey",
        "Europe/Moscow": "russia",
        "Europe/Kiev": "ukraine",
        
        # Asia
        "Asia/Tokyo": "japan",
        "Asia/Seoul": "korea",
        "Asia/Shanghai": "china",
        "Asia/Hong_Kong": "hongkong",
        "Asia/Taipei": "taiwan",
        "Asia/Singapore": "singapore",
        "Asia/Bangkok": "thailand",
        "Asia/Ho_Chi_Minh": "vietnam",
        "Asia/Jakarta": "indonesia",
        "Asia/Kuala_Lumpur": "malaysia",
        "Asia/Manila": "philippines",
        "Asia/Kolkata": "india",
        "Asia/Dhaka": "bangladesh",
        "Asia/Karachi": "pakistan",
        "Asia/Kathmandu": "nepal",
        "Asia/Colombo": "srilanka",
        "Asia/Dubai": "uae",
        "Asia/Tehran": "iran",
        "Asia/Yangon": "myanmar",
        "Asia/Tashkent": "uzbekistan",
        "Asia/Almaty": "kazakhstan",
        
        # Africa
        "Africa/Johannesburg": "southafrica",
        "Africa/Cairo": "egypt",
        "Africa/Nairobi": "kenya",
        "Africa/Lagos": "nigeria",
        "Africa/Casablanca": "morocco",
        
        # Oceania
        "Australia/Sydney": "australia",
        "Australia/Melbourne": "australia-south",
        "Australia/Brisbane": "australia-east",
        "Australia/Perth": "australia-west",
        "Australia/Adelaide": "australia-central",
        "Australia/Darwin": "australia-north",
        "Pacific/Auckland": "newzealand",
        "Pacific/Fiji": "fiji"
    }
    
    # Get short names for both timezones
    n1 = short_names.get(tz1, tz1.split("/")[-1].lower().replace("_", ""))
    n2 = short_names.get(tz2, tz2.split("/")[-1].lower().replace("_", ""))
    
    # Ensure consistent ordering for same pairs (alphabetical)
    if n1 > n2:
        n1, n2 = n2, n1
    
    return f"{n1}-{n2}"

def main():
    os.makedirs("output_html", exist_ok=True)
    
    print(f"Generating HTML files for {len(popular_pairs)} timezone combinations...")
    
    for tz1, tz2 in popular_pairs:
        # Build options:
        timezone1_options = build_options(selected_val=tz1, include_empty=False)
        timezone2_options = build_options(selected_val=tz2, include_empty=False)
        timezone3_options = build_options(selected_val=None, include_empty=True)

        name1_display = dict(timezones).get(tz1, tz1)
        name2_display = dict(timezones).get(tz2, tz2)
        slug = slugify(tz1, tz2)

        html_content = html_template.format(
            timezone1_options=timezone1_options,
            timezone2_options=timezone2_options,
            timezone3_options=timezone3_options,
            name1_display=name1_display,
            name2_display=name2_display,
            slug=slug,
        )

        filename = f"{slug}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✓ Written {filename}")

    print(f"\nGeneration complete! Created {len(popular_pairs)} HTML files.")
    print(f"Total timezones available: {len(timezones)}")

if __name__ == "__main__":
    main()