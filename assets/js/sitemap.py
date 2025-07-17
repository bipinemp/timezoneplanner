import os
from datetime import datetime

# Same timezone list from the main generator
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

# Same popular pairs from the main generator
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

def slugify(tz1, tz2):
    """Same slugify function as in the main generator"""
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
    
    n1 = short_names.get(tz1, tz1.split("/")[-1].lower().replace("_", ""))
    n2 = short_names.get(tz2, tz2.split("/")[-1].lower().replace("_", ""))
    
    # Ensure consistent ordering for same pairs (alphabetical)
    if n1 > n2:
        n1, n2 = n2, n1
    
    return f"{n1}-{n2}"

def generate_sitemap():
    """Generate sitemap.xml for all timezone combination pages"""
    # Get current date in ISO format
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Start building sitemap
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    
    <!-- Main Pages -->
    <url>
        <loc>https://timezoneplanner.netlify.app/</loc>
        <lastmod>{}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    
    <url>
        <loc>https://timezoneplanner.netlify.app/about.html</loc>
        <lastmod>{}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    
    <url>
        <loc>https://timezoneplanner.netlify.app/how-it-works.html</loc>
        <lastmod>{}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    
    <url>
        <loc>https://timezoneplanner.netlify.app/time-zone-guide.html</loc>
        <lastmod>{}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    
    <url>
        <loc>https://timezoneplanner.netlify.app/meeting-tips.html</loc>
        <lastmod>{}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>
    
    <url>
        <loc>https://timezoneplanner.netlify.app/contact.html</loc>
        <lastmod>{}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.5</priority>
    </url>
    
    <url>
        <loc>https://timezoneplanner.netlify.app/privacy-policy.html</loc>
        <lastmod>{}</lastmod>
        <changefreq>yearly</changefreq>
        <priority>0.3</priority>
    </url>
    
    <url>
        <loc>https://timezoneplanner.netlify.app/terms-of-service.html</loc>
        <lastmod>{}</lastmod>
        <changefreq>yearly</changefreq>
        <priority>0.3</priority>
    </url>
    
    <!-- Timezone Combination Pages -->'''.format(current_date, current_date, current_date, current_date, current_date, current_date, current_date, current_date)
    
    # Add all timezone combination pages
    for tz1, tz2 in popular_pairs:
        slug = slugify(tz1, tz2)
        name1_display = dict(timezones).get(tz1, tz1.split("/")[-1])
        name2_display = dict(timezones).get(tz2, tz2.split("/")[-1])
        
        # Determine priority based on popularity (you can adjust this logic)
        priority = "0.9"
        if "usa" in slug or "uk" in slug or "india" in slug or "japan" in slug or "australia" in slug:
            priority = "0.9"
        elif "nepal" in slug or "singapore" in slug or "canada" in slug or "germany" in slug:
            priority = "0.8"
        else:
            priority = "0.7"
        
        sitemap_content += f'''
    <url>
        <loc>https://timezoneplanner.netlify.app/{slug}.html</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>{priority}</priority>
    </url>'''
    
    sitemap_content += '''
    
</urlset>'''
    
    return sitemap_content

def main():
    """Generate and save sitemap.xml"""
    sitemap_xml = generate_sitemap()
    
    # Write sitemap to file
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    
    print(f"✓ Generated sitemap.xml with {len(popular_pairs)} timezone combination pages")
    print(f"✓ Total URLs in sitemap: {len(popular_pairs) + 8}")  # +8 for main pages
    print("✓ Sitemap saved as 'sitemap.xml'")
    
    # Also generate a summary of all URLs for reference
    print("\n--- Generated URLs Summary ---")
    print("Main pages: 8")
    print(f"Timezone combinations: {len(popular_pairs)}")
    print("\nSample timezone combination URLs:")
    for i, (tz1, tz2) in enumerate(popular_pairs[:10]):
        slug = slugify(tz1, tz2)
        print(f"  • https://timezoneplanner.netlify.app/{slug}.html")
    
    if len(popular_pairs) > 10:
        print(f"  ... and {len(popular_pairs) - 10} more")

if __name__ == "__main__":
    main()