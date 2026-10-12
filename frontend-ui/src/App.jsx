
import { useState } from 'react'
import './App.css'

function App() {
  const [search, setSearch] = useState('')

  const charts = [
    {
      title: 'Sales by Product',
      image: '/charts/sales_by_product.png',
    },
    {
      title: 'Sales by Payment Method',
      image: '/charts/sales_by_payment_method.png',
    },
    {
      title: 'Sales by Region',
      image: '/charts/sales_by_region.png',
    },
  ]

  const filteredCharts = charts.filter((chart) =>
  chart.title.toLowerCase().includes(search.toLowerCase().trim()) ||
  chart.image.toLowerCase().includes(search.toLowerCase().trim())
)

  return (
    <div className="dashboard">
      <header>
        <h1>E-commerce Sales Analytics</h1>
        <p>Sales performance and business insights</p>
      </header>

      <section className="summary">
        <article>
          <h3>Top-Selling Product</h3>
          <p>Laptop</p>
        </article>

        <article>
          <h3>Top Product Sales</h3>
          <p>₹110,000</p>
        </article>

        <article>
          <h3>Top Payment Method</h3>
          <p>UPI</p>
        </article>

        <article>
          <h3>UPI Sales</h3>
          <p>₹121,000</p>
        </article>
      </section>

      <section className="chart-section">
        <div className="search-container">
          <input
            type="text"
            placeholder="Search charts: Product, Payment, Region..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            aria-label="Search charts"
          />

          {search && (
            <button
              type="button"
              onClick={() => setSearch('')}
              className="clear-button"
            >
              Clear
            </button>
          )}
        </div>

        <section className="charts">
          {filteredCharts.length > 0 ? (
            filteredCharts.map((chart) => (
              <article className="chart-card" key={chart.title}>
                <h2>{chart.title}</h2>
                <img src={chart.image} alt={chart.title} />
              </article>
            ))
          ) : (
            <p className="no-results">
              No matching charts found. Try Product, Payment, or Region.
            </p>
          )}
        </section>

        <footer className="dashboard-footer">
          <p>E-commerce Sales Analytics Dashboard</p>
        </footer>
      </section>
    </div>
  )
}

export default App
