const { DateTime } = luxon;

class MeetingPlanner {
  constructor() {
    this.validPages = [
      "france-myanmar",
      "spain-venezuela",
      "uk-usa",
      "czech-japan",
      "mexico-spain",
      "turkey-usa",
      "terms-of-service",
      "uk-usa-west",
      "hongkong-usa",
      "korea-uk",
      "colombia-netherlands",
      "egypt-usa-central",
      "brazil-switzerland",
      "usa-uzbekistan",
      "index",
      "nepal-switzerland",
      "canada-atlantic-japan",
      "singapore-usa-mountain",
      "spain-usa",
      "ukraine-usa-central",
      "finland-usa-central",
      "australia-south-uk",
      "netherlands-peru",
      "canada-poland",
      "newzealand-uk",
      "france-usa",
      "southafrica-usa",
      "austria-usa-central",
      "germany-kazakhstan",
      "singapore-usa-central",
      "germany-nigeria",
      "belgium-singapore",
      "denmark-usa",
      "germany-usa-central",
      "bangladesh-usa-central",
      "indonesia-usa",
      "usa-central-vietnam",
      "australia-north-singapore",
      "alaska-india",
      "australia-west-malaysia",
      "sweden-usa",
      "norway-usa-west",
      "contact",
      "hawaii-japan",
      "australia-usa",
      "australia-nepal",
      "india-usa",
      "italy-japan",
      "fiji-usa",
      "canada-uk",
      "japan-usa-west",
      "argentina-spain",
      "chile-hongkong",
      "canada-west-korea",
      "taiwan-usa-central",
      "japan-usa",
      "morocco-uae",
      "australia-uae",
      "pakistan-usa",
      "australia-srilanka",
      "india-uk",
      "privacy-policy",
      "canada-germany",
      "hungary-philippines",
      "philippines-uk",
      "nepal-usa",
      "canada-thailand",
      "about",
      "netherlands-usa",
      "kenya-uk",
      "ireland-japan",
      "canada-east-france",
      "australia-east-usa-west",
      "iran-uk",
      "japan-uk",
    ];

    this.initializeElements();
    this.bindEvents();
    this.updateCurrentTimes();
    this.startTimeUpdater();
  }

  initializeElements() {
    this.timezone1Select = document.getElementById("timezone1");
    this.timezone2Select = document.getElementById("timezone2");
    this.timezone3Select = document.getElementById("timezone3");
    this.workStartInput = document.getElementById("workStart");
    this.workEndInput = document.getElementById("workEnd");
    this.findButton = document.getElementById("findMeetingTimes");
    this.resultsSection = document.getElementById("results");
    this.searchInput = document.getElementById("countrySearch");
    this.searchBtn = document.getElementById("searchBtn");
    this.timeFormatSelect = document.getElementById("timeFormat");
    this.timeFormat = this.timeFormatSelect.value; // default
    this.suggestionsList = document.getElementById("searchSuggestions");
  }

  bindEvents() {
    this.timezone1Select.addEventListener("change", () =>
      this.updateCurrentTimes()
    );
    this.timezone2Select.addEventListener("change", () =>
      this.updateCurrentTimes()
    );
    this.timezone3Select.addEventListener("change", () =>
      this.updateCurrentTimes()
    );
    this.findButton.addEventListener("click", () => this.findMeetingTimes());
    this.timeFormatSelect.addEventListener("change", () => {
      this.timeFormat = this.timeFormatSelect.value;
      this.updateCurrentTimes();
      this.findMeetingTimes();
    });
    this.searchInput.addEventListener("input", () =>
      this.showSearchSuggestions()
    );
    this.searchInput.addEventListener("keydown", (e) =>
      this.handleSearchKeyDown(e)
    );
    document.addEventListener("click", (e) => this.handleOutsideClick(e));
  }

  showSearchSuggestions() {
    const query = this.searchInput.value.toLowerCase().trim();
    this.suggestionsList.innerHTML = "";

    if (!query) {
      this.suggestionsList.style.display = "none";
      return;
    }

    const matches = this.validPages.filter((filename) =>
      filename.includes(query)
    );

    if (matches.length === 0) {
      this.suggestionsList.style.display = "none";
      return;
    }

    matches.forEach((filename) => {
      const li = document.createElement("li");
      li.textContent = this.formatFilenameToLabel(filename);

      li.setAttribute("tabindex", "0");
      li.style.padding = "0.5rem";
      li.style.cursor = "pointer";
      li.addEventListener("click", () => {
        window.location.href = `${filename}.html`;
      });
      li.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
          window.location.href = `${filename}.html`;
        }
      });
      this.suggestionsList.appendChild(li);
    });

    this.suggestionsList.style.display = "block";
  }
  formatFilenameToLabel(filename) {
    const regionKeywords = new Set([
      "west",
      "east",
      "north",
      "south",
      "central",
      "mountain",
      "atlantic",
    ]);

    const parts = filename.replace(/\.html$/, "").split("-");

    // Special pages
    if (
      [
        "index",
        "about",
        "contact",
        "privacy-policy",
        "terms-of-service",
      ].includes(filename)
    ) {
      return parts.map((p) => this.capitalizeCountryCode(p)).join(" ");
    }

    let countries = [];
    let region = null;

    for (const part of parts) {
      if (regionKeywords.has(part.toLowerCase())) {
        region = this.capitalizeRegion(part);
      } else {
        countries.push(this.capitalizeCountryCode(part));
      }
    }

    // If more than 2 countries, just join all with " / ", and put region at the end
    const countryPart = countries.join(" / ");
    return region ? `${countryPart} (${region})` : countryPart;
  }

  capitalizeCountryCode(code) {
    const specialCases = {
      usa: "USA",
      uk: "UK",
      uae: "UAE",
    };

    if (specialCases[code.toLowerCase()]) {
      return specialCases[code.toLowerCase()];
    }

    return code
      .split(/[\s-]/)
      .map((part) => part.charAt(0).toUpperCase() + part.slice(1).toLowerCase())
      .join(" ");
  }

  capitalizeRegion(region) {
    const regionMap = {
      west: "West",
      east: "East",
      north: "North",
      south: "South",
      central: "Central",
      mountain: "Mountain",
      atlantic: "Atlantic",
    };

    return (
      regionMap[region.toLowerCase()] ||
      region.charAt(0).toUpperCase() + region.slice(1).toLowerCase()
    );
  }

  handleSearchKeyDown(e) {
    const items = this.suggestionsList.querySelectorAll("li");
    if (!items.length) return;

    let index = Array.from(items).findIndex(
      (item) => item === document.activeElement
    );

    if (e.key === "ArrowDown") {
      e.preventDefault();
      const next = items[(index + 1) % items.length];
      next.focus();
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      const prev = items[(index - 1 + items.length) % items.length];
      prev.focus();
    }
  }

  handleOutsideClick(e) {
    if (
      !this.searchInput.contains(e.target) &&
      !this.suggestionsList.contains(e.target)
    ) {
      this.suggestionsList.style.display = "none";
    }
  }

  updateCurrentTimes() {
    this.updateTimezoneDesc("timezone1", "timezone1-desc");
    this.updateTimezoneDesc("timezone2", "timezone2-desc");
    if (this.timezone3Select.value) {
      this.updateTimezoneDesc("timezone3", "timezone3-desc");
    }
  }

  updateTimezoneDesc(selectId, descId) {
    const select = document.getElementById(selectId);
    const desc = document.getElementById(descId);

    if (select.value) {
      const now = DateTime.now().setZone(select.value);
      const timeString = now.toFormat(
        this.timeFormat === "12" ? "hh:mm a" : "HH:mm"
      );
      const dateString = now.toFormat("MMM dd, yyyy");
      desc.textContent = `Current time: ${timeString} (${dateString})`;
    } else {
      desc.textContent = "Select a timezone to see current time";
    }
  }

  startTimeUpdater() {
    setInterval(() => {
      this.updateCurrentTimes();
    }, 60000); // Update every minute
  }

  findMeetingTimes() {
    const timezones = [
      this.timezone1Select.value,
      this.timezone2Select.value,
      this.timezone3Select.value,
    ].filter((tz) => tz);

    if (timezones.length < 2) {
      alert("Please select at least two timezones");
      return;
    }

    const workStart = this.parseTime(this.workStartInput.value);
    const workEnd = this.parseTime(this.workEndInput.value);

    const results = this.calculateMeetingTimes(timezones, workStart, workEnd);
    this.displayResults(results, timezones);
  }

  parseTime(timeString) {
    const [hours, minutes] = timeString.split(":").map(Number);
    return hours * 60 + minutes; // Convert to minutes since midnight
  }

  calculateMeetingTimes(timezones, workStart, workEnd) {
    const results = [];
    const baseDate = DateTime.now().startOf("day");

    // Generate time slots every 30 minutes during potential work hours (6 AM to 10 PM)
    for (let hour = 6; hour <= 22; hour++) {
      for (let minute = 0; minute < 60; minute += 30) {
        const timeSlot = {
          hour,
          minute,
          times: [],
          inWorkHours: 0,
          quality: "poor",
        };

        timezones.forEach((tz) => {
          const dt = baseDate.set({ hour, minute }).setZone(tz);
          const minutesFromMidnight = dt.hour * 60 + dt.minute;

          timeSlot.times.push({
            timezone: tz,
            time: dt.toFormat(this.timeFormat === "12" ? "hh:mm a" : "HH:mm"),
            date: dt.toFormat("MMM dd"),
            inWorkHours:
              minutesFromMidnight >= workStart &&
              minutesFromMidnight <= workEnd,
          });

          if (
            minutesFromMidnight >= workStart &&
            minutesFromMidnight <= workEnd
          ) {
            timeSlot.inWorkHours++;
          }
        });

        // Determine quality based on how many timezones are in work hours
        if (timeSlot.inWorkHours === timezones.length) {
          timeSlot.quality = "optimal";
        } else if (timeSlot.inWorkHours >= Math.ceil(timezones.length / 2)) {
          timeSlot.quality = "good";
        }

        results.push(timeSlot);
      }
    }

    // Sort by quality and then by number of timezones in work hours
    return results
      .filter((slot) => slot.inWorkHours > 0)
      .sort((a, b) => {
        const qualityOrder = { optimal: 3, good: 2, poor: 1 };
        if (qualityOrder[a.quality] !== qualityOrder[b.quality]) {
          return qualityOrder[b.quality] - qualityOrder[a.quality];
        }
        return b.inWorkHours - a.inWorkHours;
      })
      .slice(0, 12); // Show top 12 results
  }

  displayResults(results, timezones) {
    if (results.length === 0) {
      this.resultsSection.innerHTML = `
                <h3>No Overlapping Work Hours Found</h3>
                <p>Try adjusting your work hours or consider asynchronous communication methods.</p>
            `;
    } else {
      const timezoneNames = timezones.map((tz) =>
        this.getTimezoneDisplayName(tz)
      );

      this.resultsSection.innerHTML = `
                <h3>Best Meeting Times</h3>
                <p>Showing optimal meeting times for ${timezoneNames.join(
                  ", "
                )}</p>
                <div class="time-grid">
                    ${results
                      .map((slot) => this.createTimeSlotHTML(slot))
                      .join("")}
                </div>
                <div class="legend" style="margin-top: 2rem; padding: 1rem; background: #f7fafc; border-radius: 8px;">
                    <h4>Legend:</h4>
                    <div style="display: flex; gap: 2rem; margin-top: 0.5rem; flex-wrap: wrap;">
                        <div><span style="color: #48bb78;">●</span> Optimal (all participants in work hours)</div>
                        <div><span style="color: #ed8936;">●</span> Good (most participants in work hours)</div>
                        <div><span style="color: #f56565;">●</span> Fair (some participants in work hours)</div>
                    </div>
                </div>
            `;
    }

    this.resultsSection.classList.add("show");
    this.resultsSection.scrollIntoView({ behavior: "smooth" });
  }

  createTimeSlotHTML(slot) {
    const qualityLabels = {
      optimal: "Optimal",
      good: "Good",
      poor: "Fair",
    };

    return `
            <div class="time-slot ${slot.quality}">
                <div class="slot-quality" style="font-weight: bold; color: ${this.getQualityColor(
                  slot.quality
                )}; margin-bottom: 0.5rem;">
                    ${qualityLabels[slot.quality]} Time
                </div>
                ${slot.times
                  .map(
                    (time) => `
                    <div class="time-entry" style="margin-bottom: 0.5rem;">
                        <div style="font-weight: 600;">${this.getTimezoneDisplayName(
                          time.timezone
                        )}</div>
                        <div style="font-size: 1.1rem; ${
                          time.inWorkHours
                            ? "color: #48bb78;"
                            : "color: #a0aec0;"
                        }">${time.time}</div>
                        <div style="font-size: 0.9rem; color: #4a5568;">${
                          time.date
                        }</div>
                    </div>
                `
                  )
                  .join("")}
            </div>
        `;
  }

  getQualityColor(quality) {
    const colors = {
      optimal: "#48bb78",
      good: "#ed8936",
      poor: "#f56565",
    };
    return colors[quality];
  }

  getTimezoneDisplayName(timezone) {
    const names = {
      "America/New_York": "New York",
      "America/Los_Angeles": "Los Angeles",
      "Europe/London": "London",
      "Asia/Kathmandu": "Kathmandu",
      "Asia/Kolkata": "Mumbai/Delhi",
      "Asia/Tokyo": "Tokyo",
      "Australia/Sydney": "Sydney",
      "Europe/Berlin": "Berlin",
      "Asia/Singapore": "Singapore",
      "Asia/Manila": "Manila",
    };
    return names[timezone] || timezone;
  }
}

// Initialize the meeting planner when the page loads
document.addEventListener("DOMContentLoaded", () => {
  new MeetingPlanner();
});

// Add some utility functions for better UX
document.addEventListener("DOMContentLoaded", () => {
  // Add loading states
  const findButton = document.getElementById("findMeetingTimes");
  const originalText = findButton.textContent;

  findButton.addEventListener("click", () => {
    findButton.textContent = "Finding Best Times...";
    findButton.disabled = true;

    setTimeout(() => {
      findButton.textContent = originalText;
      findButton.disabled = false;
    }, 1000);
  });

  // Add keyboard navigation for quick links
  document.querySelectorAll(".quick-link").forEach((link) => {
    link.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        link.click();
      }
    });
  });
});
